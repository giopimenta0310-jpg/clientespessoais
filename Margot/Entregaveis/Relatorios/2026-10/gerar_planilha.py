import json,csv,html,re,zipfile
from pathlib import Path
from xml.sax.saxutils import escape
R=Path(__file__).parent

def num(v):
 if isinstance(v,(int,float)):return v
 if not isinstance(v,str):return None
 s=v.strip()
 if re.fullmatch(r'[\d,]+',s):return int(s.replace(',',''))
 return None

def rows_from(doc):
 if isinstance(doc,list):return doc
 if isinstance(doc,dict):
  for key in ['result','rows','post_rows','posts','dados','dados_brutos']:
   if key in doc:
    rr=rows_from(doc[key])
    if rr:return rr
 return []

rows=[]
for fn in ['coleta-posts-links-diretos-lote3.json','coleta-posts-links-diretos-lote4.json','coleta-validacao-final-30-10.json']:
 p=R/fn
 if not p.exists():continue
 for d in rows_from(json.loads(p.read_text())):
  url=d.get('canonical_url') or d.get('url') or d.get('post_url')
  if not url or 'instagram.com' not in url:continue
  row={'titulo':d.get('description') or d.get('caption_beginning') or d.get('caption_excerpt') or d.get('caption') or d.get('title') or 'Identificação pendente', 'url':url,'data':d.get('date_posted') or d.get('published_date') or d.get('post_date') or d.get('date') or '', 'formato':d.get('post_type') or d.get('format') or '', 'views':num(d.get('views') or d.get('views_total')), 'likes':num(d.get('likes')),'comments':num(d.get('comments')),'shares':num(d.get('shares')),'saves':num(d.get('saves')),'reposts':num(d.get('reposts')),'follows':num(d.get('follows_from_post') or d.get('follows_attributed') or d.get('profile_follows') or d.get('follows')),'profile_visits':num(d.get('profile_visits')),'link_taps':num(d.get('external_link_taps',d.get('link_taps'))),'address_taps':num(d.get('business_address_taps',d.get('address_taps'))),'viewers':num(d.get('viewers',d.get('unique_viewers'))),'interactions':num(d.get('interactions')),'accounts_engaged':num(d.get('accounts_engaged')),'watchtime_raw':str(d.get('average_watch_time') or ''),'notes':d.get('notes') or d.get('note') or d.get('limitations') or d.get('unavailable_reason') or d.get('reason') or '', 'fonte':fn}
  for key in ['notes']:
   if isinstance(row[key],(list,dict)):row[key]=json.dumps(row[key],ensure_ascii=False)
  if 'unverified' in str(row['data']).lower() or '10 DE OUTUBRO' in str(row['data']):row['data']=''
  if 'DfHzM02B0jL' in url and fn=='coleta-posts-links-diretos-lote4.json':
   for k in ['views','likes','comments','shares','saves','reposts','follows','profile_visits','link_taps','address_taps','viewers','interactions','accounts_engaged']:row[k]=None
   row.update(titulo='Reel recente — identificação pendente',data='',notes='Extração retornou Affogato de outra publicação; associação rejeitada, métricas pendentes.')
  old=next((x for x in rows if x['url']==url),None)
  if old:
   for k,v in row.items():
    if v is not None and v!='':old[k]=v
  else:rows.append(row)

names={'De1xr7PB7Zg':'Um date sem pressa','De674w-Ffo5':'Open Coffee','DfAE695lTBi':'Oficina de crochê','DfCpseZlUC1':'Halloween — foto do fantasminha','DfGXMpYt-T0':'Halloween — fantasia e brigadeiro','DfHzM02B0jL':'Halloween — Reel recente (título a confirmar)','DekSEjAhVmM':'Affogato','DeaqblfjL1x':'Registros da inauguração','DeVZvucMMhq':'A casa ganhou vida','DeSBGnePbAi':'História da Margô — parte 2','DePjkcxB6iU':'Diário de obra','DeIC1L7hR2J':'História da Margô — parte 1','DezM8c_FTTE':'Bruna apresenta a choux','DeuDUIDlWFP':'A mesinha da janela','DemExxmBWwP':'Depoimentos e desejos','DeMw3nclde2':'Programação da abertura','DeUCzVMFZHa':'Joinville, é hoje','DeCzTYjt_TS':'Colaboração Bemestar'}
for row in rows:
 for key,name in names.items():
  if key in row['url']:row['titulo']=name
 if row['formato'] in ['Carousel item (photo)','Carousel Post']:row['formato']='Carrossel'
 if 'DezM8c' in row['url']:row['notes']+=' | Tempo de exibição sem unidade; alcance não validado.'
 if 'DfHzM02B0jL' in row['url']:
  row['notes']='Dados da validação final; Reel recente confirmado, título ainda a conferir.'
  row['data']='30/10/2026 (conferir timestamp no fechamento)'
account=json.loads((R/'coleta-validacao-final-30-10.json').read_text())['dados']['account_metrics']
account_table=[['Métrica','Valor','Período/observação'],['Visualizações',account['views'],account['date_range']],['Viewers',account['viewers'],'Rótulo original; não rebatizado como alcance'],['Interações',account['interactions'],'Total exibido'],['Contas engajadas',account['accounts_engaged'],'Pessoas/contas distintas do total de interações'],['Visitas ao perfil',account['profile_visits'],'Não são visitas físicas'],['Toques no link',account['external_link_taps'],'Não são vendas confirmadas'],['Toques no endereço',account['business_address_taps'],'Não são visitas físicas'],['Seguidores atuais',account['total_followers'],'Snapshot do perfil, não crescimento no período'],['Ganhos/perdas líquidos',None,'Indisponível'],['Views de não seguidores (%)',account['views_non_followers_pct'],'Distribuição das visualizações'],['Views Stories (%)',account['format_shares_views']['stories'],'Distribuição por formato'],['Views Posts (%)',account['format_shares_views']['posts'],'Distribuição por formato'],['Views Reels (%)',account['format_shares_views']['reels'],'Distribuição por formato']]
headers={'titulo':'Conteúdo','data':'Data exibida','formato':'Formato','url':'Publicação','views':'Visualizações','likes':'Curtidas','comments':'Comentários','shares':'Compartilhamentos','saves':'Salvamentos','reposts':'Reposts','follows':'Seguidores atribuídos','profile_visits':'Visitas ao perfil','link_taps':'Toques no link','address_taps':'Toques no endereço','viewers':'Viewers (rótulo bruto)','interactions':'Interações (rótulo bruto)','accounts_engaged':'Contas engajadas','watchtime_raw':'Tempo médio bruto — não calcular sem unidade','notes':'Observações','fonte':'Fonte de coleta'}
with (R/'publicacoes-coleta-30-10.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f,delimiter=';');w.writerow(headers.values());w.writerows([[r.get(k) for k in headers] for r in rows])
(R/'publicacoes-normalizadas-30-10.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')

# XLSX com stdlib: dados, fontes e folha para atualização sem apagar o corte inicial.
def col(i):
 s=''
 while i:i,m=divmod(i-1,26);s=chr(65+m)+s
 return s

def sheet_xml(table):
 out=['<?xml version="1.0" encoding="UTF-8" standalone="yes"?><worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetViews><sheetView workbookViewId="0"><pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" state="frozen"/></sheetView></sheetViews><cols>']
 for i in range(1,len(table[0])+1):out.append(f'<col min="{i}" max="{i}" width="{42 if i in [1,4,19,20] else 21}" customWidth="1"/>')
 out.append('</cols><sheetData>')
 for ri,row in enumerate(table,1):
  out.append(f'<row r="{ri}">')
  for ci,v in enumerate(row,1):
   if v is None or v=='':continue
   ref=col(ci)+str(ri);style=1 if ri==1 else 0
   if isinstance(v,(int,float)):out.append(f'<c r="{ref}" s="{style}"><v>{v}</v></c>')
   else:out.append(f'<c r="{ref}" s="{style}" t="inlineStr"><is><t xml:space="preserve">{escape(str(v))}</t></is></c>')
  out.append('</row>')
 out.append(f'</sheetData><autoFilter ref="A1:{col(len(table[0]))}{len(table)}"/></worksheet>')
 return ''.join(out)
meta=[['Item','Registro'],['Conta','@margocafesespeciais'],['Data de corte','30/10/2026 — America/Sao_Paulo'],['Estado','Coleta parcial; sem fechamento definitivo'],['Linhas individuais identificadas',len(rows)],['Janela geral','Últimos 30 dias; datas exatas a conferir na interface'],['Insights individuais','Acumulados exibidos; janela deve ser validada'],['Vazios','Métrica indisponível ou não validada; não significa zero'],['Seguidores','Total não equivale a crescimento'],['Alcance','Views e viewers não foram convertidos em alcance'],['Watchtime','Valor sem unidade não usado para análise'],['Pago x orgânico','Não confirmado; seguidores/não seguidores não substitui esse dado'],['Corte final','Nova checagem manual planejada com Giovanna em 31/10'],['Privacidade','Arquivos locais, fora do GitHub público']]
check=[['Publicação','Métrica','Valor em 30/10','Valor na checagem','Data/hora da checagem','Observações']]
for row in rows:
 for k in ['views','shares','saves','follows','profile_visits']:
  check.append([row['url'],headers[k],row[k],None,None,'Preservar mesmo rótulo e período'])
sheets=[('Conta — 30 dias',account_table),('Publicações', [list(headers.values())]+[[r.get(k) for k in headers] for r in rows]),('Método e cobertura',meta),('Checagem 31-10',check)]
ns='http://schemas.openxmlformats.org/spreadsheetml/2006/main'
with zipfile.ZipFile(R/'Margo-metricas-coleta-30-10.xlsx','w',zipfile.ZIP_DEFLATED) as z:
 z.writestr('[Content_Types].xml','<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/><Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>'+''.join(f'<Override PartName="/xl/worksheets/sheet{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>' for i in range(1,len(sheets)+1))+'</Types>')
 z.writestr('_rels/.rels','<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>')
 z.writestr('xl/workbook.xml',f'<workbook xmlns="{ns}" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets>'+''.join(f'<sheet name="{escape(name)}" sheetId="{i}" r:id="rId{i}"/>' for i,(name,_) in enumerate(sheets,1))+'</sheets></workbook>')
 z.writestr('xl/_rels/workbook.xml.rels','<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'+''.join(f'<Relationship Id="rId{i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{i}.xml"/>' for i in range(1,len(sheets)+1))+f'<Relationship Id="rId{len(sheets)+1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/></Relationships>')
 z.writestr('xl/styles.xml',f'<styleSheet xmlns="{ns}"><fonts count="2"><font><sz val="11"/><name val="Calibri"/></font><font><b/><sz val="11"/><name val="Calibri"/></font></fonts><fills count="3"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill><fill><patternFill patternType="solid"><fgColor rgb="FFFFADC9"/><bgColor indexed="64"/></patternFill></fill></fills><borders count="1"><border/></borders><cellStyleXfs count="1"><xf/></cellStyleXfs><cellXfs count="2"><xf fontId="0" fillId="0" borderId="0" xfId="0" applyAlignment="1"><alignment vertical="top" wrapText="1"/></xf><xf fontId="1" fillId="2" borderId="0" xfId="0" applyFont="1" applyFill="1" applyAlignment="1"><alignment vertical="top" wrapText="1"/></xf></cellXfs></styleSheet>')
 for i,(_,table) in enumerate(sheets,1):z.writestr(f'xl/worksheets/sheet{i}.xml',sheet_xml(table))
print('Publicações normalizadas:',len(rows))
