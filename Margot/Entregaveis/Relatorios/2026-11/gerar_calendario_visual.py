from pathlib import Path
import calendar,json,csv,re
from html import escape
r=Path(__file__).resolve().parent
report=r.parent/'2026-10'
data=json.loads((r/'CALENDARIO_NOVEMBRO_v01.json').read_text())
posts=data['conteudos']
posts=[p for p in posts if p['Data de publicação']!='01/11/2026']
posts.insert(0,{'Data de publicação':'01/11/2026','Dia':'Domingo','Conteúdo':'Pets e crianças','Formato':'Estático','Situação da data':'Data definida','Orientação':'Foto única de pet e criança; uso da imagem autorizado pela família, conforme confirmado anteriormente.'})
data.update(status='Datas definidas: 01 e 03/11. Favoritos com datas sugeridas.',conteudos=posts)
(r/'CALENDARIO_NOVEMBRO_v02.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
with (r/'CALENDARIO_NOVEMBRO_v02.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(posts[0]),delimiter=';');w.writeheader();w.writerows(posts)
byday={int(p['Data de publicação'][:2]):p for p in posts}
weekdays=['DOM','SEG','TER','QUA','QUI','SEX','SÁB']
grid='<div class="month-grid">'+''.join('<div class="weekday">'+d+'</div>' for d in weekdays)
for week in calendar.Calendar(firstweekday=6).monthdayscalendar(2026,11):
 for day in week:
  if not day:grid+='<div class="day outside"></div>';continue
  p=byday.get(day)
  cls='day';inner=''
  if p:
   state=p['Situação da data'];cls+=' defined' if state=='Data definida' else (' suggested' if state=='Data sugerida' else ' open')
   if state=='Espaço em aberto':inner='<div class="post-title muted">Pauta a definir</div>'
   else:inner=f'<div class="post-title">{escape(p["Conteúdo"].replace("Reel · ",""))}</div><div class="post-format">{escape(p["Formato"])}</div>'
  grid+=f'<div class="{cls}"><div class="day-number">{day:02d}</div>{inner}</div>'
grid+='</div>'
css='''<style>.calendar h1{font-size:36px;margin:14px 0 8px}.calendar .intro{font-size:16px;margin-bottom:10px}.month-grid{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:6px}.weekday{font-size:12px;font-weight:bold;letter-spacing:1px;padding:3px 8px;color:#617157}.day{height:80px;border:1px solid #d5dbc9;background:#faf9f4;padding:6px 9px;position:relative;overflow:hidden}.day-number{font-size:14px;font-weight:bold;margin-bottom:3px;color:#65745b}.post-title{font-size:15px;line-height:1.15;font-weight:bold}.post-format{font-size:12px;line-height:1.2;margin-top:4px}.day.defined{background:#e1e9d5;border-left:4px solid #597347}.day.suggested{background:#f4e4ec;border-left:4px solid #a36687}.day.open{background:#fffaf4;border-style:dashed}.day.outside{border-color:transparent;background:transparent}.muted{color:#8a9283;font-weight:normal;font-size:13px}.calendar .takeaway{font-size:15px;padding:10px 16px;bottom:45px;display:flex;gap:22px;background:transparent;border-top:1px solid #d5dbc9}.key::before{content:'';display:inline-block;width:11px;height:11px;margin-right:7px;background:#e1e9d5;border:1px solid #597347}.key.suggest::before{background:#f4e4ec;border-color:#a36687}.key.pending::before{background:#fffaf4;border:1px dashed #999}.calendar .foot{font-size:11px;bottom:20px}</style>'''
slide='<section class="slide calendar" id="calendario"><div class="mast"><span>Margô · Calendário de conteúdo</span><span>Novembro 2026</span></div><h1>Novembro · calendário de posts.</h1><p class="intro">Pets e crianças em 01/11 · yoga em 03/11 · favoritos distribuídos como proposta para aprovação.</p>'+grid+'<div class="takeaway"><span class="key">Data definida</span><span class="key suggest">Data sugerida</span><span class="key pending">Pauta em aberto</span></div><div class="foot">Dias sem conteúdo seguem livres. Publicação de yoga em 03/11; data da oficina não informada. Datas dos favoritos podem ser ajustadas.</div></section>'
html=(report/'RESUMO_DIAGNOSTICO_E_CALENDARIO_v02.html').read_text()
html,count=re.subn(r'<section class="slide calendar".*?</section>',lambda m:slide,html,flags=re.S)
assert count==1
html=html.replace('</style><body>','</style><body>'+css,1) if '</style><body>' in html else html.replace('<body>','<body>'+css,1)
(report/'RESUMO_DIAGNOSTICO_E_CALENDARIO_v03.html').write_text(html)
# Standalone page uses the same layout as the report, with only the month visible.
head=html.split('<body>')[0]
(r/'CALENDARIO_NOVEMBRO_VISUAL_v02.html').write_text(head+'<body>'+css+slide+'</body></html>')
md='# Calendário de novembro · versão 02\n\nDatas definidas: pets e crianças em 01/11 (estático), Reel da oficina de yoga em 03/11. Datas dos favoritos são sugestões.\n\n| Data | Dia | Conteúdo | Formato | Situação |\n|---|---|---|---|---|\n'
for p in posts:md+='| '+' | '.join(str(p[k]) for k in ['Data de publicação','Dia','Conteúdo','Formato','Situação da data'])+' |\n'
md+='\nOs dias sem conteúdo estão livres; pautas a definir não são publicações confirmadas.\n'
(r/'CALENDARIO_NOVEMBRO_v02.md').write_text(md)
(report/'RESUMO_DIAGNOSTICO_E_CALENDARIO_v03.md').write_text((report/'RESUMO_DIAGNOSTICO_OUTUBRO_v01.md').read_text()+'\n\n---\n\n'+md)
assert calendar.weekday(2026,11,1)==6
assert len([p for p in posts if 'Favoritos' in p['Conteúdo']])==6
print('Calendário visual atualizado: 01/11 incluído; domingo na primeira coluna; 30 dias do mês e seis favoritos preservados.')
