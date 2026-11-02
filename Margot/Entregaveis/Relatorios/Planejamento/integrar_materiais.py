# Executado pelo gerador após consolidar datas e conceitos; material não altera aprovação.
inventory=json.loads((R/'Inventario-Drive/inventario-editorial.json').read_text())
raw=json.loads((R/'Inventario-Drive/inventario-bruto-31-10.json').read_text())
folders={x['title']:x['url'] for x in raw['root'] if x['mime_type']=='application/vnd.google-apps.folder'}
groups={g['topic']:g for g in inventory['groups']}
def grouped(topic,status=None):
 g=groups[topic]
 return dict(status=status or g['state'],files=g['files']+' Seleção: '+g['selection'],next=g['pending'],folder=g['folder'],url=folders.get(g['folder'],inventory['root']),preview='Inventario-Drive/'+g['contact'],checked='2026-10-31')
def other(status,files,next):
 return dict(status=status,files=files,next=next,checked='2026-10-31')
material={
 '2026-11-01':other('Localizar no acervo anterior','Foto de pet e criança autorizada, citada no histórico; fora deste Drive.','Localizar o original usado no planejamento; não é indicação de nova captação.'),
 '2026-11-03':other('Existe em outro lugar','Reel da yoga confirmado pela Giovanna como existente em outro local.','Reunir o arquivo/link para edição; não precisa gravar novamente por falta nesta pasta.'),
 '2026-11-05':grouped('Favoritos da Bruna'),
 '2026-11-07':grouped('Croque Meu Senhor'),
 '2026-11-10':other('Localizar no acervo anterior','17-10: A001_10171624_C022.MOV, citado no histórico; não reaberto nesta rodada.','Localizar e conferir uso anterior, imagem e áudio. Os vídeos do mocha não substituem o coado.'),
 '2026-11-12':grouped('Preparo do mocha'),
 '2026-11-14':other('Material parcial · conceito a decidir','Drive: sete vídeos da massa do red velvet (C025–C031); sem finalização ou serviço nos quadros revisados.','Para manter o salgado da cozinha à mesa, captar finalização e serviço. Alternativa com acervo: bastidor da massa do red velvet, somente se decidirmos adaptar a pauta.'),
 '2026-11-17':grouped('Favoritos da Suelen'),
 '2026-11-19':other('Localizar no acervo anterior','17-10: IMG_2979–2981, fatia de red velvet citada no histórico. O Drive atual tem só vídeos da massa.','Localizar fatia, conferir qualidade e uso anterior. Choux aberta é reserva possível, sem substituir automaticamente.'),
 '2026-11-21':other('Precisa captar','Não foram localizadas cenas de pessoas trabalhando no Drive revisado.','Gravar pessoa trabalhando, café chegando e contexto da casa; confirmar condições vigentes do Open Coffee.'),
 '2026-11-24':other('Material parcial · localizar composição','Croque novo: IMG_3307–3309/3311. Composição e red velvet: acervo 17-10, IMG_2979–2982 e IMG_2990–2994, ainda a localizar.','Conferir combinação completa, recortes e uso anterior. Não anunciar como combo promocional.'),
 '2026-11-26':other('Ainda não gravado','Giovanna confirmou que os favoritos do Marcos ainda não foram gravados.','Captar fala, pedidos escolhidos, detalhes e fotos. Aproveitar a sessão também para o carrossel de 17/12.'),
 '2026-11-28':grouped('Mesa para grupos'),
 '2026-11-30':other('Imagem disponível · regras pendentes','Mesa do Grupo: IMG_3315/3316 ou IMG_3318/3320 podem ilustrar o convite.','Definir quantidade de pessoas, benefício e condições. Divulgação para encontros futuros; não anuncia atendimento na segunda-feira.'),
 '2026-12-08':grouped('Favoritos da Bruna'),
 '2026-12-17':other('Ainda não gravado','Mesma captação pendente dos favoritos do Marcos de 26/11.','Gravar fala e fotos na mesma sessão, separando o enfoque do Reel e do carrossel.'),
 '2026-12-29':grouped('Favoritos da Suelen'),
 '2026-12-03':other('Imagem disponível · regras pendentes','Mesa do Grupo pode apoiar, com recorte diferente do conteúdo de novembro.','Retomar apenas com regras aprovadas e contexto novo; não repetir a mesma peça.'),
 '2026-12-15':other('Precisa captar','Troca de pedidos e reações não localizadas no Drive revisado.','Duas pessoas, pedidos diferentes, enquadramento fixo, olhares, troca e prova; data continua provisória.'),
 '2026-12-22':other('Precisa captar','Não foi localizada a finalização e o serviço de outro prato para esta pauta.','Escolher prato com a Bruna e captar finalização, textura e chegada à mesa; variar em relação a novembro.'),
 '2027-01-07':other('Depende de regras e material','Foto de grupo pode apoiar; não há sessão específica de aniversário identificada.','Confirmar benefício e condições antes da comunicação; definir se usaremos acervo ou nova captação.'),
 '2027-01-16':other('Precisa captar','Não localizada sequência de domingo com chegada, pedido e horários reais.','Anotar horários durante a gravação e captar o percurso completo; confirmar funcionamento.'),
 '2027-01-21':other('Precisa captar nova abordagem','Não foram localizados os gestos específicos desta proposta no Drive atual.','Gravar escolha conjunta, partilha e reação; diferenciar do date já publicado e da troca de pedidos.')}
for post in posts:
 post['material']=material[post['date']]
 if post['date']=='2026-11-14':post['description']='Um salgado sendo finalizado e servido. Acervo atual tem só massa de red velvet; adaptar a pauta é uma opção a decidir.'
 # Orientações atuais substituem notas operacionais antigas, preservadas na v13.
 post['notes']=post['description']+' Material em 31/10: '+post['material']['status']+'. '+post['material']['files']+' Próximo passo: '+post['material']['next']
for idea in ideas:
 id=idea['id']
 matching={'croque':'Croque Meu Senhor','mocha':'Preparo do mocha','mesa':'Mesa para grupos','cozinha':'Massa do red velvet'}
 if id in matching:
  g=groups[matching[id]]
  idea['material']=grouped(matching[id]);idea['capture']=g['files']+' '+g['selection'];idea['pending']=g['pending']
  idea['status']=g['state']
  if id=='mesa':idea['title']='Mesa para grupos';idea['angle']='Mesa vazia e grupo reunido: convite para encontros, na linha da mesa alta. Material localizado para 28/11.';idea['month']='2026-11';idea['months']=['2026-11','2026-12']
  if id=='cozinha':idea['status']='Material parcial · conceito a decidir';idea['capture']='Há vídeos de massa do red velvet. Finalização e serviço de um salgado ainda precisam de captação se mantivermos o conceito.'
for topic,id in [('Choux por dentro','choux-acervo'),('Caramelo salgado','caramelo-acervo'),('Produtos avulsos e mural','avulsos-acervo')]:
 g=groups[topic]
 ideas.append(dict(id=id,title=topic,month='2026-11',months=['2026-11','2026-12','2027-01'],format='Estático ou carrossel',status=g['state'],origin='Inventário visual do Drive · 31/10',angle=g['use'],capture=g['files']+' '+g['selection'],pending=g['pending'],source='Inventario-Drive/inventario-editorial.json',repeat='Reserva sem data: escolher um ângulo e alternar comida e bebida.',proposed_dates=[],material=grouped(topic)))
data.update(posts=posts,ideas=ideas,material_review=dict(date='2026-10-31',source=inventory['root'],method=inventory['method'],priority=inventory['priorities'],guide='Inventario-Drive/GUIA_MATERIAIS_E_PRIORIDADES.html'))
def material_badge(post):
 m=post.get('material')
 return '<div class="material-badge'+(' capture' if 'captar' in m['status'].lower() or 'não gravado' in m['status'] else '')+'">Material: '+e(m['status'])+'</div>' if m else ''
def material_print_pages():
 chunks=[posts[:7],posts[7:14],posts[14:20],posts[20:]]
 result=''
 for n,chunk in enumerate(chunks,1):
  rows=''.join('<tr><td>'+e(p['date'][8:]+'/'+p['date'][5:7])+'<br><b>'+e(p['title'])+'</b></td><td><b>'+e(p['material']['status'])+'</b><br>'+e(p['material']['files'])+'</td><td>'+e(p['material']['next'])+'</td></tr>' for p in chunk)
  result+=f'<section class="slide material-print"><div class="mast"><span>Margô · Material integrado ao calendário</span><span>{n}/{len(chunks)} · 31/10</span></div><h1>O que usar. O que falta.</h1><p class="intro">Estado do material separado da aprovação. Datas e formatos preservados. Fotos revistas em folhas de contato e seis quadros por vídeo; áudio não auditado.</p><table><tr><th>Post</th><th>Material e arquivos</th><th>Próximo passo</th></tr>{rows}</table><div class="foot">Seleção visual e links: Inventario-Drive/GUIA_MATERIAIS_E_PRIORIDADES.html. Marcos não gravado; yoga em outro lugar.</div></section>'
 return result
