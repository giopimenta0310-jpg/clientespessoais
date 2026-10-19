import AppKit
import AVFoundation
guard CommandLine.arguments.count > 2 else { fatalError("Uso: swift contatos.swift PASTA_SAIDA PASTA_BRUTOS") }
let source=URL(fileURLWithPath:CommandLine.arguments[2])
let output=URL(fileURLWithPath:CommandLine.arguments[1])
let files=(FileManager.default.enumerator(at:source,includingPropertiesForKeys:nil)!.allObjects as! [URL]).filter{["heic","mov","jpg","jpeg","png"].contains($0.pathExtension.lowercased())}.sorted{$0.path<$1.path}
var groups:[String:[(String,NSImage)]]=[:]
var inventory:[[String:Any]]=[]
for url in files {
 let group=url.deletingLastPathComponent()==source ? "Avulsos" : url.deletingLastPathComponent().lastPathComponent
 if url.pathExtension.lowercased()=="mov" {
  let asset=AVURLAsset(url:url);let duration=CMTimeGetSeconds(asset.duration)
  let gen=AVAssetImageGenerator(asset:asset);gen.appliesPreferredTrackTransform=true;gen.maximumSize=CGSize(width:500,height:500)
  inventory.append(["arquivo":url.path.replacingOccurrences(of:source.path+"/",with:""),"duracao":duration.isFinite ? duration : 0,"tipo":"video"])
  for fraction in [0.1,0.5,0.85] {
    do {let frame=try gen.copyCGImage(at:CMTime(seconds:max(0,duration*fraction),preferredTimescale:600),actualTime:nil);groups[group,default:[]].append(("\(url.lastPathComponent) · \(Int(duration*fraction))s",NSImage(cgImage:frame,size:.zero)))} catch {print("Falha \(url.lastPathComponent): \(error)")}
  }
 } else if let image=NSImage(contentsOf:url) {
  groups[group,default:[]].append((url.lastPathComponent,image))
  inventory.append(["arquivo":url.path.replacingOccurrences(of:source.path+"/",with:""),"tipo":"foto","largura":image.size.width,"altura":image.size.height])
 }
}
for (g,items) in groups {
 for start in stride(from:0,to:items.count,by:16) {
  let chunk=Array(items[start..<min(start+16,items.count)]),rows=Int(ceil(Double(chunk.count)/4)),w=1000,h=rows*250+45
  let rep=NSBitmapImageRep(bitmapDataPlanes:nil,pixelsWide:w,pixelsHigh:h,bitsPerSample:8,samplesPerPixel:4,hasAlpha:true,isPlanar:false,colorSpaceName:.deviceRGB,bytesPerRow:0,bitsPerPixel:0)!
  NSGraphicsContext.saveGraphicsState();NSGraphicsContext.current=NSGraphicsContext(bitmapImageRep:rep)
  NSColor.white.setFill();NSRect(x:0,y:0,width:w,height:h).fill()
  (g as NSString).draw(at:NSPoint(x:10,y:h-32),withAttributes:[.font:NSFont.boldSystemFont(ofSize:18),.foregroundColor:NSColor.black])
  for (i,item) in chunk.enumerated() {
   let x=CGFloat((i%4)*250),base=CGFloat(h-45-(i/4+1)*250),size=item.1.size,ratio=min(240/size.width,218/size.height)
   item.1.draw(in:NSRect(x:x+5+(240-size.width*ratio)/2,y:base+27+(218-size.height*ratio)/2,width:size.width*ratio,height:size.height*ratio))
   (item.0 as NSString).draw(in:NSRect(x:x+6,y:base+3,width:240,height:22),withAttributes:[.font:NSFont.systemFont(ofSize:12),.foregroundColor:NSColor.black])
  }
  NSGraphicsContext.restoreGraphicsState()
  let name=g.replacingOccurrences(of:"/",with:"-")+"-\(start/16+1).jpg"
  try rep.representation(using:.jpeg,properties:[.compressionFactor:0.85])!.write(to:output.appendingPathComponent(name));print(name)
 }
}
try JSONSerialization.data(withJSONObject:inventory,options:[.prettyPrinted,.sortedKeys]).write(to:output.appendingPathComponent("inventario.json"))
print("Total: \(inventory.count) arquivos")
