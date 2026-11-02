from pathlib import Path
import zipfile,xml.etree.ElementTree as ET, json,csv,calendar
from xml.sax.saxutils import escape
r=Path(__file__).resolve().parent
n=r.parent/'2026-11';n.mkdir(exist_ok=True)
rows=[['03/11/2026','Terça','Reel · oficina de yoga','Reel','Data definida','Conteúdo informado; revisar edição e copy. Não presumir que esta seja a data da oficina.'],['05/11/2026','Quinta','Favoritos da Bruna','Carrossel','Data sugerida','Apresentar escolhas e motivos; confirmar itens e disponibilidade.'],['10/11/2026','Terça','Favoritos do Marcos','Reel','Data sugerida','Usar fala e ação; complementar o carrossel sem repetir tudo.'],['12/11/2026','Quinta','Favoritos da Suelen','Carrossel','Data sugerida','Apresentar escolhas e motivos; confirmar itens e disponibilidade.'],['17/11/2026','Terça','Favoritos da Bruna','Reel','Data sugerida','Trazer a indicação pessoal e mostrar o pedido.'],['24/11/2026','Terça','Favoritos do Marcos','Carrossel','Data sugerida','Detalhar os itens e os motivos da escolha.'],['26/11/2026','Quinta','Favoritos da Suelen','Reel','Data sugerida','Trazer a indicação pessoal e mostrar o pedido.']]
headers=['Data de publicação','Dia','Conteúdo','Formato','Situação da data','Orientação']
# Open slots are proposals, not commitments to produce a new post.
for d in [7,14,19,21,28]:rows.append([f'{d:02d}/11/2026',['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo'][calendar.weekday(2026,11,d)],'A definir','A definir','Espaço em aberto','Definir pauta e material antes de confirmar a publicação.'])
rows.sort(key=lambda x:int(x[0][:2]))
(n/'CALENDARIO_NOVEMBRO_v01.json').write_text(json.dumps({'mes':'2026-11','status':'Proposta inicial; apenas 03/11 definido','conteudos': [dict(zip(headers,row)) for row in rows]},ensure_ascii=False,indent=2))
with (n/'CALENDARIO_NOVEMBRO_v01.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f,delimiter=';');w.writerow(headers);w.writerows(rows)
md='# Calendário de novembro · proposta inicial\n\nReel da oficina de yoga com publicação definida para 03/11. Datas dos favoritos são sugestões. Os materiais foram informados pela Giovanna; arquivos e edição ainda não foram conferidos nesta atualização.\n\n| Data | Dia | Conteúdo | Formato | Situação |\n|---|---|---|---|---|\n'
for row in rows:md+='| '+' | '.join(row[:5])+' |\n'
md+='\nTemos três carrosséis e três vídeos de favoritos: um de cada formato para Bruna, Marcos e Suelen. Reservas abertas não são posts confirmados. Os dias não listados seguem sem publicação definida. Não é necessário preencher todos os espaços; vamos definir as próximas pautas juntas.\n'
(n/'CALENDARIO_NOVEMBRO_v01.md').write_text(md)
# Append a real worksheet while preserving every existing ZIP entry.
src=r/'Margo-metricas-coleta-30-10.xlsx';dst=r/'Margo-relatorio-e-calendario-novembro-v01.xlsx'
with zipfile.ZipFile(src) as z:files={i.filename:z.read(i.filename) for i in z.infolist()}
ns='http://schemas.openxmlformats.org/spreadsheetml/2006/main';rn='http://schemas.openxmlformats.org/officeDocument/2006/relationships';pn='http://schemas.openxmlformats.org/package/2006/relationships';cn='http://schemas.openxmlformats.org/package/2006/content-types'
ET.register_namespace('',ns);ET.register_namespace('r',rn)
wb=ET.fromstring(files['xl/workbook.xml']);sheets=wb.find('{'+ns+'}sheets');idx=max(int(x.attrib['sheetId']) for x in sheets)+1
rel=ET.fromstring(files['xl/_rels/workbook.xml.rels']);rid='rId'+str(max(int(x.attrib['Id'][3:]) for x in rel)+1)
ET.SubElement(sheets,'{'+ns+'}sheet',{'name':'Calendário novembro','sheetId':str(idx),'{'+rn+'}id':rid})
ET.SubElement(rel,'{'+pn+'}Relationship',{'Id':rid,'Type':rn+'/worksheet','Target':f'worksheets/sheet{idx}.xml'})
ct=ET.fromstring(files['[Content_Types].xml']);ET.SubElement(ct,'{'+cn+'}Override',{'PartName':f'/xl/worksheets/sheet{idx}.xml','ContentType':'application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml'})
for name,root in [('xl/workbook.xml',wb),('xl/_rels/workbook.xml.rels',rel),('[Content_Types].xml',ct)]:files[name]=ET.tostring(root,encoding='utf-8',xml_declaration=True)
xml=f'<worksheet xmlns="{ns}"><sheetViews><sheetView workbookViewId="0"><pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" state="frozen"/></sheetView></sheetViews><cols>'+''.join(f'<col min="{i}" max="{i}" width="{width}" customWidth="1"/>' for i,width in enumerate([23,15,32,18,23,70],1))+'</cols><sheetData>'
for ri,row in enumerate([headers]+rows,1):
 xml+=f'<row r="{ri}" ht="{32 if ri==1 else 58}" customHeight="1">'
 for ci,v in enumerate(row):xml+=f'<c r="{chr(65+ci)}{ri}" s="{1 if ri==1 else 0}" t="inlineStr"><is><t>{escape(v)}</t></is></c>'
 xml+='</row>'
xml+=f'</sheetData><autoFilter ref="A1:F{len(rows)+1}"/></worksheet>'
files[f'xl/worksheets/sheet{idx}.xml']=xml.encode()
with zipfile.ZipFile(dst,'w',zipfile.ZIP_DEFLATED) as z:
 for name,data in files.items():z.writestr(name,data)
with zipfile.ZipFile(dst) as z:
 assert not z.testzip()
 for name in z.namelist():
  if name.endswith('.xml') or name.endswith('.rels'):ET.fromstring(z.read(name))
for row in rows: assert calendar.weekday(2026,11,int(row[0][:2]))==['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo'].index(row[1])
# Add one concise calendar slide to the existing diagnosis; tabs in screen view.
html=(r/'RESUMO_DIAGNOSTICO_OUTUBRO_v01.html').read_text().replace(' / 04',' / 05')
confirmed=[row for row in rows if row[2]!='A definir']
table='<table class="calendar-table"><thead><tr><th>Data</th><th>Conteúdo</th><th>Formato</th><th>Status</th></tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+escape(x)+'</td>' for x in [row[0][:5]+' · '+row[1],row[2],row[3],row[4]])+'</tr>' for row in confirmed)+'</tbody></table>'
slide='<section class="slide calendar" id="calendario"><div class="mast"><span>Margô · Calendário de novembro</span><span>05 / 05</span></div><h1>Novembro · ponto de partida.</h1><p class="intro">Yoga em 03/11 + seis conteúdos de favoritos. As demais datas são uma proposta para debate.</p>'+table+'<div class="takeaway">Próximas pautas em aberto: 07, 14, 19, 21 e 28/11. Preencher conforme material e objetivo; não são compromissos de publicação.</div><div class="foot">Planejamento inicial · 31/10/2026. Data da postagem de yoga não representa confirmação da data da oficina. Demais dias sem publicação definida.</div></section>'
extra='''<style>.calendar-table{font-size:18px;margin-top:18px}.calendar-table td,.calendar-table th{padding:8px 14px}.calendar-table td:first-child{width:19%}.calendar-table td:nth-child(2){width:40%}.tabs{display:none}@media screen{.tabs{display:flex;gap:10px;position:sticky;top:0;z-index:10;background:#fffaf4;padding:14px 56px;border-bottom:1px solid #bac6ac}.tabs button{padding:10px 18px;border:1px solid #bac6ac;background:#edf0e3;border-radius:7px;color:#273923;cursor:pointer;font-size:16px}.tabs button.active{background:#273923;color:white}.slide{margin:0 auto}.slide.hidden{display:none}}@media print{.tabs{display:none}.slide.hidden{display:block}}</style>'''
nav='<nav class="tabs"><button class="active" onclick="showTab(false,this)">Diagnóstico de outubro</button><button onclick="showTab(true,this)">Calendário de novembro</button></nav>'
js='''<script>function showTab(cal,button){document.querySelectorAll('.slide').forEach(s=>s.classList.toggle('hidden',s.classList.contains('calendar')!==cal));document.querySelectorAll('.tabs button').forEach(b=>b.classList.toggle('active',b===button));window.scrollTo(0,0)}if(!matchMedia('print').matches)document.querySelector('.calendar').classList.add('hidden');</script>'''
html=html.replace('<body>','<body>'+extra+nav).replace('</body>',slide+js+'</body>')
(r/'RESUMO_DIAGNOSTICO_E_CALENDARIO_v02.html').write_text(html)
(r/'RESUMO_DIAGNOSTICO_E_CALENDARIO_v02.md').write_text((r/'RESUMO_DIAGNOSTICO_OUTUBRO_v01.md').read_text()+'\n\n---\n\n'+md)
print('Aba adicionada à planilha; HTML com duas abas e slide de calendário preparados. Datas e XML validados.')
