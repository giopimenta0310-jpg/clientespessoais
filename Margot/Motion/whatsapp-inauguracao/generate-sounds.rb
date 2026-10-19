rate=44100
srand(42)
write=lambda{|name,duration,&wave|data=Array.new((rate*duration).to_i){|i|v=wave.call(i.to_f/rate);[[v,-1.0].max,1.0].min*26000}.map(&:to_i).pack('s<*');File.binwrite("public/sounds/#{name}.wav",'RIFF'+[36+data.bytesize].pack('V')+'WAVEfmt '+[16,1,1,rate,rate*2,2,16].pack('VvvVVvv')+'data'+[data.bytesize].pack('V')+data)}
write.call('tap',0.18){|t|Math.sin(2*Math::PI*640*t)*Math.exp(-t*80)*0.35}
write.call('send',0.35){|t|Math.sin(2*Math::PI*(460*t+1200*t*t))*Math.exp(-t*19)*0.4}
write.call('receive',0.45){|t|a=Math.sin(2*Math::PI*920*t)*Math.exp(-t*23);u=[t-0.09,0].max;b=t>0.09 ? Math.sin(2*Math::PI*1240*u)*Math.exp(-u*20) : 0;(a+b)*0.28}
write.call('notification',0.8){|t|[0,0.16].sum{|offset|u=t-offset;u>=0 ? (Math.sin(2*Math::PI*(offset==0 ? 880 : 1175)*u)+0.25*Math.sin(2*Math::PI*1760*u))*Math.exp(-u*10)*0.3 : 0}}
write.call('typing',2.2){|t|period=0.105;u=t%period;Math.sin(2*Math::PI*(1100+((t/period).to_i%4)*120)*u)*Math.exp(-u*170)*0.3+(rand-0.5)*Math.exp(-u*200)*0.2}
write.call('whoosh',0.8){|t|(rand-0.5)*Math.sin(Math::PI*t/0.8)**2*0.25}
