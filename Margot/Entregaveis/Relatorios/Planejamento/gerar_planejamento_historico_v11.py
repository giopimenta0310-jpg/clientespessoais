from pathlib import Path
import json,calendar,re,math
from html import escape as e
R=Path(__file__).resolve().parent
base=R.parent/'2026-11'
old=json.loads((base/'CALENDARIO_NOVEMBRO_v02.json').read_text())
posts=[]
for p in old['conteudos']:
 d=p['Data de publicação']; iso=d[6:]+'-'+d[3:5]+'-'+d[:2]
 posts.append(dict(date=iso,title=p['Conteúdo'].replace('Reel · ',''),format=p['Formato'],status='Definido' if p['Situação da data']=='Data definida' else ('Em aberto' if p['Situação da data']=='Espaço em aberto' else 'Proposta'),notes=p['Orientação'],source='Conversa com Giovanna · 31/10'))
ideas=[
dict(id='amigo',title='Amigo secreto na casa',month='2026-11',format='Carrossel',status='Regras pendentes',origin='Bruna · mensagem enviada em 31/10',angle='Antecipar os encontros de fim de ano. Retomar em dezembro se fizer sentido.',capture='Grupo reunido, mesa e café para compartilhar; preparar as condições aprovadas.',pending='Definir X pessoas, quantidade/tamanho da prensa, condições de consumo, validade e operação. Não anunciar café grátis antes da aprovação.',source='Mensagem anexada nesta conversa',repeat='Novembro e dezembro; rever a ação a cada fim de ano.'),
dict(id='aniversario',title='Aniversário com a turma',month='2026-12',format='Carrossel',status='Regras pendentes',origin='Bruna · mensagem enviada em 31/10',angle='Um motivo recorrente para reunir amigos na casa. Mês sugerido para desenvolver, sem data de publicação.',capture='Mesa de celebração, bebida, doce e salgado; condições aprovadas.',pending='Definir X acompanhantes, itens e limites do benefício, comprovação/período do aniversário, consumo e validade. Não prometer conta inteira grátis.',source='Mensagem anexada nesta conversa',repeat='Ideia permanente; reavaliar para janeiro e meses seguintes, sem obrigação de repostar todo mês.'),
dict(id='croque',title='Croque em detalhe',month='2026-11',format='Estático',status='Checar uso anterior',origin='Reserva de conteúdo · 22/10',angle='Destacar o gratinado e o pedido salgado, além do ambiente.',capture='Acervo 17-10: Sobre a mesa que mais tem clientes/IMG_2982.HEIC; alternativa IMG_2990.HEIC.',pending='Conferir se já foi publicado e se o prato segue disponível. Evitar repetir o mesmo recorte da mesinha.',source='Replanejamento-19-outubro/PROPOSTAS_RESERVA_27_E_29_OUTUBRO.md',repeat='Pode retornar com outra foto/gesto e contexto.'),
dict(id='coado',title='Antes do primeiro gole',month='2026-11',format='Reel',status='Checar uso anterior',origin='Reserva de conteúdo · 22/10',angle='O ritual do preparo: água entrando no filtro e a pausa começando no balcão.',capture='Acervo 17-10: A001_10171624_C022.MOV. Trecho inicial sugerido no histórico: conferir entre 4 e 12 s.',pending='Conferir publicação anterior, arquivo contínuo e áudio. Não chamar de ASMR sem ouvir.',source='Replanejamento-19-outubro/PROPOSTAS_RESERVA_27_E_29_OUTUBRO.md',repeat='Ritual de café pode virar repertório com novas captações.'),
dict(id='mesa',title='Outro cantinho em uso',month='2026-12',format='Carrossel',status='Nova captação',origin='Diagnóstico editorial de outubro',angle='Pausa sozinha, leitura ou encontro em um lugar reconhecível.',capture='Plano aberto, pessoa com pedido, detalhe da vista e da mesa.',pending='Captar uma situação diferente da mesinha já publicada; autorização de quem aparece.',source='RELATORIO_EDITORIAL_OUTUBRO_v03.md · ambiente e experiência',repeat='Alternar ocasiões e cantinhos, conforme material.'),
dict(id='open',title='Open Coffee acontecendo',month='2026-11',format='Reel',status='Nova captação',origin='Vídeo previsto após divulgação + diagnóstico',angle='Uma tarde real de trabalho na casa, além do anúncio da oferta.',capture='Pessoa trabalhando, café chegando, detalhe do pedido e ambiente.',pending='Confirmar condições vigentes e captar rotina real antes de fechar a data.',source='CONTEXTO_ATUAL.md · Open Coffee / diagnóstico outubro',repeat='Mostrar usos reais em vez de repetir só a arte de serviço.'),
dict(id='combinacao',title='Croque, red velvet e café',month='2026-12',format='Carrossel',status='Checar uso anterior',origin='Replanejamento de 19/10',angle='Da vontade de salgado ao doce, mostrando uma composição possível.',capture='Acervo: IMG_2979–2982, IMG_2990–2994; conferir recortes e qualidade.',pending='Checar uso anterior, disponibilidade e repetição em relação ao Croque e à mesinha. Não é combo promocional.',source='Replanejamento-19-outubro/calendario-e-copies-v04.md',repeat='Uma alternativa ao Croque isolado, não duas peças iguais na mesma semana.'),
dict(id='domingo',title='Um domingo de manhã na casa',month='2027-01',format='Reel',status='Nova captação',origin='Calendário de operação · proposta antiga',angle='Chegar, escolher a mesa, pedir e ficar um pouco.',capture='Entrada, luz da manhã, caminho, pedido e pessoas vivendo a pausa.',pending='Reconfirmar horário; não chamar de brunch, buffet ou café da manhã completo sem oferta confirmada.',source='calendario-operacao-17-a-31-outubro-2026-v01.md',repeat='Ocasião de visita que pode reaparecer com novas cenas.'),
dict(id='date',title='Date: dividindo o pedido',month='2027-01',format='Reel',status='Nova abordagem',origin='Diagnóstico editorial de outubro',angle='Uma ação específica: escolher juntos ou negociar a última garfada.',capture='Dupla real, escolha, prato compartilhado e reação.',pending='Nova captação e execução diferente do date anterior; não é pauta já comprovada.',source='RELATORIO_EDITORIAL_OUTUBRO_v03.md · date',repeat='Testar antes de decidir se vira série.'),
dict(id='encontro',title='O encontro que aconteceu',month='2026-12',format='Carrossel',status='Depende de evento',origin='Diagnóstico editorial de outubro',angle='Oficina/encontro real contado por momentos e participantes.',capture='Atividade, mãos, pessoas e detalhes; falas se acrescentarem algo.',pending='Escolher evento que realmente aconteça, conferir acervo e autorizações; nenhuma nova oficina está confirmada.',source='RELATORIO_EDITORIAL_OUTUBRO_v03.md · receitas editoriais',repeat='Depois de encontros confirmados, sem inventar uma agenda.')]
ideas[0]['months']=['2026-11','2026-12']
ideas[1]['months']=['2026-12','2027-01']
changes={7:('Croque em detalhe','Estático','Proposta · checar uso','Recuperado do histórico: confirmar publicação anterior e disponibilidade antes de usar.'),14:('Amigo secreto na casa','Carrossel','Regras pendentes','Ideia da Bruna. Sugestão de data; depende das regras comerciais aprovadas. Se não houver definição, substituir a pauta.'),19:('Antes do primeiro gole','Reel','Proposta · checar uso','Recuperado do histórico. Conferir publicação anterior e edição do arquivo do coado.'),21:('Open Coffee em uso','Reel','Captação pendente','Proposta do histórico/diagnóstico. Captar uma tarde real; se não houver material, manter em aberto.')}
for p in posts:
 day=int(p['date'][-2:])
 if day in changes:
  p.update(zip(['title','format','status','notes'],changes[day]));p['source']={7:'Histórico · reserva de 22/10',14:'Bruna · mensagem de 31/10',19:'Histórico · reserva de 22/10',21:'Histórico e diagnóstico de outubro'}[day]
# Direção da Bruna: dar protagonismo a doces e salgados no feed.
for post in posts:
 if post['date']=='2026-11-19':post.update(title='Red velvet em detalhe',format='Estático',status='Proposta · checar uso',notes='Substitui o Reel de coado para ampliar comida no feed. Acervo IMG_2979–2981: conferir uso anterior, qualidade e disponibilidade.',source='Bruna · pedido de mais comida + histórico 17-10')
 if post['date']=='2026-11-28':post.update(title='Da cozinha à mesa',format='Reel',status='Captação pendente',notes='Proposta: um salgado em finalização, corte e serviço. Escolher item disponível com a Bruna; não há nova gravação conferida.',source='Proposta editorial a partir do pedido da Bruna')
 if post['title'].startswith('Favoritos'):
  post['notes']+=' Direção: dar protagonismo aos pratos, doces e salgados realmente escolhidos; confirmar escolhas. Não inventar favoritos nem exigir que cada pessoa escolha o mesmo tipo de item.'
for idea in ideas:
 if idea['id']=='coado':idea['month']='2026-12';idea['angle']+=' Guardado sem data; a proposta de 19/11 passa a ser red velvet para equilibrar o feed.'
 if idea['id'] in ['mesa','domingo','date','encontro','open','amigo','aniversario']:
  idea['capture']+=' Quando coerente com a cena, mostrar comida reconhecível e pessoas comendo, além das bebidas; alimentação no Open Coffee continua à parte.' if idea['id']=='open' else ' Incluir doces ou salgados reconhecíveis quando coerente com a pauta.'
ideas.extend([
 dict(id='redvelvet',title='Red velvet em detalhe',month='2026-11',months=['2026-11','2026-12'],format='Estático',status='Checar uso anterior',origin='Bruna · mais comida no feed + acervo de outubro',angle='Foco na fatia, nas camadas e na textura. Um doce como protagonista.',capture='Acervo 17-10: IMG_2979–2981; conferir recortes e resolução. Se não servir, fotografar fatia e detalhe.',pending='Conferir uso anterior e disponibilidade; evitar a mesma sequência do carrossel da mesinha.',source='Replanejamento-19-outubro/calendario-e-copies-v04.md + pedido da Bruna nesta conversa',repeat='Alternar doces e salgados em vez de repetir só bebidas.'),
 dict(id='cozinha',title='Da cozinha à mesa',month='2026-11',months=['2026-11','2026-12','2027-01'],format='Reel',status='Nova captação',origin='Nova proposta a partir do pedido da Bruna',angle='Um prato disponível: finalização, corte ou textura e o pedido chegando à mesa.',capture='Escolher prato com a Bruna; captar preparo/finalização, detalhe e serviço. Preferir salgado para alternar com o doce.',pending='Confirmar produto e nova captação. Não afirmar que esses planos já existem no acervo.',source='Pedido da Bruna nesta conversa · 31/10/2026',repeat='Repertório recorrente de comida, mudando o prato e o gesto.')])
editorial_direction={'goal':'Mostrar café especial e cozinha autoral com comida visível no feed.', 'guideline':'Proposta de cadência: ao menos uma pauta com doce ou salgado protagonista por semana, conforme material e aprovação.', 'favorites':'Priorizar os itens de comida que os sócios realmente escolheram. Escolhas ainda precisam ser conferidas.', 'november_food_dates':['2026-11-07','2026-11-19','2026-11-28'], 'note':'Favoritos podem reforçar comida, mas não contam como escolhas confirmadas de pratos. Bebidas, pessoas e experiência continuam no calendário.'}
data={'version':4,'updated':'2026-10-31','posts':posts,'ideas':ideas,'editorial_direction':editorial_direction,'scope':'Novembro parcialmente definido; dezembro e janeiro são reservatórios de ideias sem datas fechadas.'}
# Revisão v06: três favoritos em novembro e três em dezembro, intercalados com o banco.
previous_posts={p['date']:dict(p) for p in posts}
favorite_moves={'2026-11-05':'2026-11-05','2026-11-24':'2026-12-17','2026-11-12':'2026-11-26','2026-11-17':'2026-12-08','2026-11-10':'2026-11-17','2026-11-26':'2026-12-29'}
for post in posts:
 original=post['date']
 if original in favorite_moves:
  post['date']=favorite_moves[original]
  post['notes']+=' Série espaçada: três favoritos por mês, em novembro e dezembro, com outras pautas entre as publicações. Data sugerida, ainda não aprovada.'
# As vagas de novembro recebem propostas do banco, sem confirmar nova captação.
ideas_by_id={i['id']:i for i in ideas}
def bank_post(date,idea_id,title=None,status=None,extra=''):
 idea=ideas_by_id[idea_id]
 return dict(date=date,title=title or idea['title'],format=idea['format'],status=status or ('Proposta · checar uso' if 'Checar' in idea['status'] else ('Regras pendentes' if 'Regras' in idea['status'] else 'Captação pendente')),notes=idea['angle']+' Captar: '+idea['capture']+' Pendente: '+idea['pending']+' '+extra,source=idea['source'],bankIdeaId=idea_id)
# 28/11 muda de cozinha para convite a um domingo; o Reel de cozinha vai a 24/11.
posts=[p for p in posts if p['date']!='2026-11-28']
posts.extend([
 bank_post('2026-11-10','mesa',extra='Mostrar um pedido salgado na cena, se houver material; usar outro ângulo/situação da casa.'),
 bank_post('2026-11-12','combinacao',extra='Usar composição completa, sem repetir os recortes do Croque de 07/11; conferir disponibilidade e uso anterior.'),
 bank_post('2026-11-24','cozinha'),
 bank_post('2026-12-10','coado'),
 bank_post('2026-11-28','domingo',extra='Publicação sugerida no sábado como convite para um domingo. Confirmar funcionamento antes da copy.'),
 bank_post('2026-12-03','amigo',extra='Retomada apenas se campanha, regras e validade estiverem aprovadas; não repetir a arte de novembro sem novo contexto.'),
 bank_post('2026-12-22','cozinha',title='Da cozinha à mesa · outro prato',extra='Uma nova escolha de salgado, sem reaproveitar a mesma edição de novembro.'),
 bank_post('2027-01-07','aniversario'),
 bank_post('2027-01-21','date')])
posts.sort(key=lambda p:p['date'])
for idea_id,months in {'mesa':['2026-11','2026-12'],'coado':['2026-12'],'combinacao':['2026-11','2026-12'],'domingo':['2026-11','2027-01']}.items():
 idea=ideas_by_id[idea_id];idea['months']=months;idea['month']=months[0]
ideas_by_id['coado']['angle']='O ritual do preparo: água entrando no filtro e a pausa começando no balcão. Proposta para 10/12, entre favoritos e conteúdos de comida; conferir uso anterior.'
for idea in ideas:idea['proposed_dates']=[p['date'] for p in posts if p.get('bankIdeaId')==idea['id'] or p['title']==idea['title']]
favorites=[p for p in posts if p['title'].startswith('Favoritos')]
from datetime import date
favorite_dates=sorted(date.fromisoformat(p['date']) for p in favorites)
assert len(favorites)==6 and all((b-a).days>=9 for a,b in zip(favorite_dates,favorite_dates[1:]))
assert len({p['date'] for p in posts})==len(posts)
assert all(sum(p['date'].startswith(month) for p in favorites)==3 for month in ['2026-11','2026-12'])
assert not any(p['date'].startswith('2027-01') for p in favorites)
editorial_direction.update(favorites_spacing='Três favoritos por mês: novembro e dezembro. Intervalo entre favoritos: 9 a 12 dias nesta proposta. Janeiro mantém outras ideias do banco.',november_food_dates=['2026-11-07','2026-11-12','2026-11-19','2026-11-24'])
# v08: aproveitar o mocha gravado e equilibrar café com doces e salgados.
for post in posts:
 if post['date']=='2026-11-12':
  post.update(title='Mocha em preparo',format='Reel',status='Material gravado · edição pendente',notes='Giovanna informou que gravou a produção de mocha. Selecionar etapas reais e a bebida pronta; arquivo, áudio e qualidade ainda não conferidos nesta atualização.',source='Giovanna · gravação de mocha informada em 31/10',bankIdeaId='mocha')
posts.append(bank_post('2026-12-15','combinacao',extra='Transferida de 12/11 para abrir espaço ao mocha gravado. Não é combo promocional; conferir recortes já usados e disponibilidade.'))
posts.sort(key=lambda p:p['date'])
ideas_by_id['combinacao']['month']='2026-12';ideas_by_id['combinacao']['months']=['2026-12'];ideas_by_id['combinacao']['proposed_dates']=['2026-12-15']
ideas.append(dict(id='mocha',title='Mocha em preparo',month='2026-11',format='Reel',status='Material gravado · edição pendente',origin='Giovanna · nova gravação informada em 31/10',angle='Mostrar as etapas reais do preparo e terminar na bebida pronta, dando vontade de provar.',capture='Produção de mocha já gravada pela Giovanna; localizar o arquivo e selecionar os planos aproveitáveis.',pending='Conferir arquivo, áudio, enquadramento e edição. Não inventar ingredientes ou etapas que não apareçam.',source='Mensagem da Giovanna nesta conversa',repeat='Reaproveitar a estrutura com outras bebidas, alternando com doces e salgados.',proposed_dates=['2026-11-12']))
editorial_direction.update(goal='Equilibrar café e cozinha autoral no feed, com bebidas, doces e salgados reconhecíveis.',guideline='Alternar pautas de café e comida ao longo das semanas; evitar sequências repetidas. Manter espaço para pessoas e experiência, sem exigir divisão rígida de 50/50.',november_food_dates=['2026-11-07','2026-11-19','2026-11-24'],november_coffee_dates=['2026-11-12','2026-11-21'])
# v09: conceitos escolhidos pela Giovanna a partir da pesquisa.
for post in posts:
 if post['date']=='2026-11-10':
  post.update(title='O seu parece melhor',format='Reel',status='Conceito escolhido · captação pendente',bankIdeaId='troca',source='Giovanna · escolha da ideia 3 da pesquisa de 31/10',notes='Substitui o carrossel de cantinho. Duas pessoas sentadas recebem pedidos diferentes, olham para o pedido uma da outra e trocam os pratos/xícaras; terminar provando. Mostrar comida e café com produtos disponíveis. Captar enquadramento fixo, troca e reações; não foi confirmado que esses planos existam no acervo. Conceito escolhido; data e edição permanecem propostas.')
 if post['date']=='2026-11-28':
  post.update(title='Domingo em pequenos horários',format='Reel',status='Conceito escolhido · captação pendente',source='Giovanna · escolha da ideia 5 da pesquisa de 31/10',notes='Mini-vlog: chegada à casa, escolha da mesa, pedido, café e comida chegando, tempo para ficar. Horários reais discretos na tela, anotados durante a gravação; sem inventar horários ou nova oferta. Data sugerida de publicação no sábado, convidando para um domingo. Confirmar funcionamento e captar a experiência. Conceito escolhido; arquivo/cenas ainda não auditados.')
ideas_by_id['mesa']['month']='2026-12';ideas_by_id['mesa']['months']=['2026-12'];ideas_by_id['mesa']['proposed_dates']=[]
ideas_by_id['mesa']['angle']+=' O carrossel de 10/11 foi substituído pela troca de pedidos; esta versão de cantinho fica no banco de dezembro, sem data.'
ideas_by_id['domingo'].update(title='Domingo em pequenos horários',angle='Mini-vlog com horários reais na tela: chegada, escolha da mesa, pedido, café e comida, tempo de ficar.',capture='Planos em ordem da experiência e horários anotados durante a captação. Mostrar bebida e comida; falas não são obrigatórias.',pending='Confirmar funcionamento e gravar cenas do domingo. Não inventar horários nem anunciar brunch/buffet.',status='Conceito escolhido · captação pendente',source='Calendário de outubro + ideia 5 da pesquisa de 31/10, escolhida pela Giovanna',proposed_dates=['2026-11-28'])
ideas.append(dict(id='troca',title='O seu parece melhor',month='2026-11',format='Reel',status='Conceito escolhido · captação pendente',origin='Giovanna · escolha da ideia 3 da pesquisa',angle='Duas pessoas recebem pedidos diferentes, olham o da outra e trocam os pratos/xícaras antes de provar. Uma ação leve de casal/amigas na mesa.',capture='Duas pessoas e dois pedidos disponíveis; plano fixo mostrando ambos, olhares, troca e primeira prova. Combinar comida e café conforme os pedidos reais.',pending='Gravar a troca e as reações; acervo existente não confirmado para essa sequência. Data sugerida, sem agendamento.',source='Pesquisas/REFERENCIAS_CAFETERIAS_31-10-2026.md · Meal swap adaptado e escolhido pela Giovanna',repeat='Usar outra situação caso o tema de encontro volte em janeiro; não repetir a mesma troca/edição.',proposed_dates=['2026-11-10']))
# A proposta de janeiro continua como reserva, com variação a decidir.
ideas_by_id['date']['pending']+=' Considerar uma execução diferente da troca escolhida para novembro, antes de produzir a proposta de janeiro.'
# v10: a foto da mesa para grupos ocupa 28/11; domingo fica mais adiante.
for post in posts:
 if post['date']=='2026-11-28':
  sunday=dict(post);sunday.update(date='2027-01-16',status='Conceito escolhido · captação pendente',notes=post['notes']+' Adiado por pedido da Giovanna; 16/01 é apenas uma sugestão de data, substituindo 28/11.')
  posts.append(sunday)
  post.update(title='Mesa para grupos',format='Carrossel',status='Definido',bankIdeaId='mesa',source='Giovanna · foto da mesa para grupos e data de 28/11',notes='Usar a foto da mesa para grupos que a Giovanna informou ter tirado. Seguir a proposta da mesa alta: mostrar um lugar reconhecível e convidar para reunir pessoas, com café e comida quando houver material. Arquivo da foto ainda não recebido/conferido nesta rodada. Capa baseada na foto; detalhes de mesa/pedidos só se houver imagens de apoio. A data foi definida pela Giovanna; arte e copy ainda serão produzidas.')
  break
posts.sort(key=lambda p:p['date'])
ideas_by_id['mesa'].update(title='Mesa para grupos',month='2026-11',months=['2026-11','2026-12'],status='Foto informada · produção pendente',angle='Carrossel na linha da mesa alta: foto da mesa para grupos e convite para reunir amigos, conversar e compartilhar uma pausa.',capture='Giovanna informou uma foto nova da mesa para grupos. Localizar e conferir o arquivo; usar detalhes e pedidos apenas se houver imagens adequadas.',pending='Conferir foto e apoios, definir composição e copy. Não inventar capacidade, reserva, promoção ou pedido obrigatório.',source='Pedido da Giovanna nesta conversa · mesa para grupos em 28/11',proposed_dates=['2026-11-28'])
ideas_by_id['domingo'].update(month='2027-01',months=['2027-01'],proposed_dates=['2027-01-16'])
assert len({p['date'] for p in posts})==len(posts)
# v11: amigo secreto no final de novembro, intercalado com os favoritos.
for post in posts:
 if post['date']=='2026-11-14' and post['title']=='Amigo secreto na casa':
  post['date']='2026-11-24';post['notes']+=' Divulgação transferida para o final de novembro, conforme pedido da Giovanna. Regras comerciais continuam pendentes.'
 elif post['date']=='2026-11-24' and post['title']=='Da cozinha à mesa':
  post['date']='2026-11-14';post['notes']+=' Antecipado para ocupar a vaga do amigo secreto. Captação permanece pendente.'
posts.sort(key=lambda p:p['date'])
for idea in ideas:
 if idea['id'] in ['amigo','cozinha']:
  idea['proposed_dates']=[p['date'] for p in posts if p.get('bankIdeaId')==idea['id'] or p['title']==idea['title']]
editorial_direction['november_food_dates']=['2026-11-07','2026-11-14','2026-11-19']
assert len({p['date'] for p in posts})==len(posts)
descriptions={
 'Mesa para grupos':'Foto da mesa para grupos, na linha da mesa alta, convidando a reunir amigos.',
 'O seu parece melhor':'Duas pessoas recebem pedidos diferentes, olham o da outra, trocam os pratos e provam.',
 'Domingo em pequenos horários':'Mini-vlog da chegada ao pedido, com café, comida e horários reais.',
 'Mocha em preparo':'Mostrar as etapas do mocha gravadas por você e finalizar com a bebida pronta.',
 'Pets e crianças':'Foto de pet e criança para mostrar que os dois são bem-vindos.',
 'oficina de yoga':'Mostrar momentos da oficina e a experiência na casa; conferir o material disponível.',
 'Croque em detalhe':'Close no gratinado para dar vontade de pedir um salgado.',
 'Outro cantinho em uso':'Alguém aproveitando uma mesa com um pedido, para imaginar uma pausa ali.',
 'Croque, red velvet e café':'Mostrar salgado, doce e café como uma escolha de pedido — sem ser combo.',
 'Amigo secreto na casa':'Convidar grupos a fazer o encontro na casa; benefício ainda depende das regras.',
 'Red velvet em detalhe':'Foto da fatia e das camadas, com o doce como protagonista.',
 'Open Coffee em uso':'Uma tarde real de trabalho: notebook, café chegando e a casa em movimento.',
 'Da cozinha à mesa':'Mostrar um salgado sendo finalizado e chegando à mesa; precisa gravar.',
 'Um domingo de manhã na casa':'Chegar de manhã, escolher a mesa, fazer um pedido e aproveitar sem pressa.',
 'Antes do primeiro gole':'Um Reel do preparo do coado: a água no filtro e o café sendo feito.',
 'Da cozinha à mesa · outro prato':'Novo prato e outra finalização, sem repetir a edição de novembro.',
 'Aniversário com a turma':'Convidar para celebrar com amigos; a promoção ainda precisa de regras.',
 'Date: dividindo o pedido':'Uma dupla escolhendo e provando do pedido do outro, com reações reais.'}
for post in posts:
 if post['title'].startswith('Favoritos'):
  who=post['title'].split(' ')[-1]
  post['description']=(f'{who} apresenta os pedidos preferidos e por que gosta deles.' if post['format']=='Carrossel' else f'{who} conta sua escolha enquanto mostramos o pedido de perto.')
 else:post['description']=descriptions.get(post['title'],'Ideia em aberto; definir abordagem e material.')
data.update(version=11,posts=posts,ideas=ideas,editorial_direction=editorial_direction,scope='Proposta distribuída de novembro a janeiro. 01/11, 03/11 e 28/11 são datas definidas; demais dependem de aprovação e, quando indicado, material/regras.')
(R/'PLANEJAMENTO_MARGO_v11.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
# Reuse the established report styles and its four diagnostic slides.
oldhtml=(R.parent/'2026-10/RESUMO_DIAGNOSTICO_OUTUBRO_v01.html').read_text()
head=oldhtml.split('<body>')[0]
diag=oldhtml.split('<body>')[1].split('</body>')[0]
css='''<style>@page{size:338.667mm 275.167mm}.month{height:1040px}.post-description{font-size:12px;line-height:1.2;margin:4px 0;color:#4d6046}.toolbar{padding:16px 35px;position:sticky;top:0;background:#fffaf4;z-index:10;border-bottom:1px solid #cad2be;display:flex;flex-wrap:wrap;gap:8px;align-items:center}.toolbar button,.toolbar select,.toolbar label{font-size:15px;padding:9px 12px;border:1px solid #bac6ac;background:#edf0e3;color:#273923;border-radius:6px;cursor:pointer}.toolbar button.active{background:#273923;color:white}.view{display:none}.view.active{display:block}.month h1{font-size:34px;margin:13px 0 8px}.month .intro{font-size:15px;margin-bottom:9px}.month-grid{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:5px}.weekday{font-size:11px;letter-spacing:1px;font-weight:bold;padding:3px 8px}.day{height:140px;border:1px solid #d5dbc9;padding:5px 8px;background:#faf9f4;overflow:hidden}.day-number{font-size:12px;font-weight:bold;margin-bottom:3px;color:#617157}.post-title{font-size:12px;font-weight:bold;line-height:1.12}.post-format{font-size:11px;margin-top:3px;line-height:1.1}.day.defined{background:#e1e9d5;border-left:4px solid #597347}.day.proposal{background:#f4e4ec;border-left:4px solid #a36687}.day.pending{background:#fff0d8;border-left:4px solid #bb8b34}.day.empty{background:transparent;border-style:dashed}.day.outside{background:transparent;border-color:transparent}.six .day{height:122px;padding:4px 7px}.six .day-number{font-size:11px;line-height:1.1;margin-bottom:2px}.six .post-title{font-size:13px;line-height:1.1}.six .post-description{font-size:12px;line-height:1.22;margin:5px 0}.six .post-format{font-size:11px;white-space:nowrap;margin-top:2px}.month .takeaway{font-size:14px;padding:9px 13px;bottom:43px}.month .foot{bottom:18px}.idea-strip{margin-top:12px;padding:10px 13px;background:#edf0e3;font-size:14px;line-height:1.3}.hint{font-size:12px;font-weight:normal;color:#617157}.bank{max-width:1180px;margin:30px auto;padding:0 20px}.bank article{min-height:0;margin-bottom:15px;padding:20px}.bank h2{margin:8px 0 12px}.bank p{font-size:17px;margin-bottom:8px}.bank small{font-size:13px}.form-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}.form-grid label{font-size:16px}.form-grid input,.form-grid select,.form-grid textarea{display:block;width:100%;padding:10px;border:1px solid #bac6ac;font:16px Arial;margin-top:5px}.form-grid .wide{grid-column:1/-1}form button{padding:12px 20px;background:#273923;color:white;border:0;font-size:16px;margin:15px 0}.notice{font-size:15px;padding:15px;background:#f1dfe7}.bank-print table{font-size:15px;margin-top:18px}.bank-print td,.bank-print th{padding:10px}.bank-print .intro{font-size:18px}.bank-print h1{font-size:34px}.print-only{display:none}button{cursor:pointer}@media screen{body{background:#eeeae2}.slide{background:#fffaf4;margin:15px auto;box-shadow:0 2px 15px #0001}.bank{background:#fffaf4;padding:25px}.bank article button{font-size:13px;margin-right:8px}.month .day:not(.outside){cursor:pointer}}@media print{.toolbar,.bank,.screen-only{display:none!important}.view{display:block!important}.print-only{display:block}.slide{break-after:page}.slide:last-child{break-after:auto}.month .day{cursor:default}}</style>'''

def monthslide(y,m,live=False):
 items=[p for p in posts if p['date'].startswith(f'{y}-{m:02d}')]
 by={int(p['date'][-2:]):p for p in items}
 weeks=calendar.Calendar(6).monthdayscalendar(y,m)
 grid='<div class="month-grid'+(' six' if len(weeks)==6 else '')+'">'+''.join('<div class="weekday">'+x+'</div>' for x in ['DOM','SEG','TER','QUA','QUI','SEX','SÁB'])
 for week in weeks:
  for day in week:
   if not day:grid+='<div class="day outside"></div>';continue
   p=by.get(day);state=p['status'] if p else ''
   cls='defined' if state=='Definido' else ('pending' if ('pendente' in state.lower() or 'checar' in state.lower()) else ('proposal' if state=='Proposta' else 'empty'))
   content=(f'<div class="post-title">{e(p["title"])}</div><div class="post-description">{e(p["description"])}</div><div class="post-format">{e(p["format"])}'+(' · pendente' if cls=='pending' else '')+'</div>') if p and state!='Em aberto' else ''
   grid+=f'<div class="day {cls}" data-date="{y}-{m:02d}-{day:02d}"><div class="day-number">{day:02d}</div>{content}</div>'
 grid+='</div>'
 names={11:'Novembro',12:'Dezembro',1:'Janeiro'};name=names[m]
 ideasmonth=[i['title'] for i in ideas if f'{y}-{m:02d}' in i.get('months',[i['month']])]
 strip='' if m==11 or len(weeks)==6 else '<div class="idea-strip"><b>Banco de ideias · referência:</b> '+e(' · '.join(ideasmonth[:3])+(' · +'+str(len(ideasmonth)-3)+' ideias no banco' if len(ideasmonth)>3 else ''))+'</div>'
 intro='Definidos: pets/crianças 01/11, yoga 03/11 e mesa para grupos 28/11. Três favoritos no mês, com outras pautas entre eles. Demais datas são propostas.' if m==11 else ('Três favoritos no mês, intercalados com pautas do banco. Datas sugeridas, sujeitas a aprovação.' if m==12 else 'Ideias do banco para janeiro. Sem favoritos nesta proposta; datas sugeridas, sujeitas a aprovação.')
 return f'<section class="slide month"><div class="mast"><span>Margô · Calendário de conteúdo</span><span>{name} {y}</span></div><h1>{name} · {y}.</h1><p class="intro">{intro}</p>{grid}{strip}<div class="takeaway">Verde: data definida · Rosa: proposta · Amarelo: depende de regra, material ou checagem.</div><div class="foot">Direção: alternar café, doces e salgados, com pessoas e experiência. Favoritos: confirmar escolhas reais. Promoções seguem pendentes de regras.</div></section>'
months=''.join(monthslide(y,m) for y,m in [(2026,11),(2026,12),(2027,1)])
# A short print bank; detailed briefs remain in the interactive bank and JSON.
bankpages=''
for part in range(math.ceil(len(ideas)/5)):
 subset=ideas[part*5:(part+1)*5]
 rows=''.join('<tr><td>'+e(i['title'])+'</td><td>'+e(i['month'])+'<br>'+e(i['status'])+'</td><td>'+e(i['pending'])+'</td></tr>' for i in subset)
 bankpages+=f'<section class="slide bank-print"><div class="mast"><span>Margô · Banco de ideias</span><span>{part+1}/{math.ceil(len(ideas)/5)}</span></div><h1>Ideias para guardar e desenvolver.</h1><p class="intro">Origem registrada no arquivo editável. Meses e datas sugeridas não significam publicação aprovada.</p><table><tr><th>Ideia</th><th>Mês / estado</th><th>Antes de produzir</th></tr>{rows}</table><div class="foot">Aniversário é uma ideia recorrente. Amigo secreto pode ser retomado em dezembro. Nenhuma regra promocional está aprovada nesta versão.</div></section>'
script=R/'app.js'
nav='<nav class="toolbar"><button onclick="tab(\'diagnostico\',this)">Diagnóstico</button><button class="active" onclick="tab(\'calendario\',this)">Calendário</button><button onclick="tab(\'ideias\',this)">Banco de ideias</button><span id="month-controls"><button onclick="stepMonth(-1)">←</button><select id="month-select" onchange="selectMonth(this.value)"></select><button onclick="stepMonth(1)">→</button></span><button onclick="exportData()">Exportar ideias</button><label>Importar JSON<input type="file" id="import" accept=".json" hidden></label></nav>'
form='''<div class="bank"><h1>Banco de ideias.</h1><p class="notice"><b>Direção editorial:</b> equilíbrio entre café, comida e favoritos espaçados (três por mês, em novembro e dezembro). Alternar bebidas, doces e salgados; favoritos mostram escolhas reais, sem inventar itens.</p><p class="notice">As alterações ficam salvas neste navegador. Exporte o JSON para guardar uma cópia ou levar a outro computador. Este arquivo não agenda nem publica posts.</p><div id="idea-list"></div><h2 id="form-title">Guardar uma nova ideia</h2><form id="idea-form"><div class="form-grid"><label>Título<input name="title" required></label><label>Mês de interesse<input name="month" type="month" required value="2026-12"></label><label>Formato<input name="format" placeholder="Reel, carrossel, estático..."></label><label>Estado<input name="status" value="Ideia guardada"></label><label>Origem<input name="origin" placeholder="Bruna, histórico, nova sugestão..."></label><label>Data sugerida (opcional)<input name="date" type="date"></label><label class="wide">Ideia / abordagem<textarea name="angle" rows="2"></textarea></label><label class="wide">O que captar<textarea name="capture" rows="2"></textarea></label><label class="wide">O que falta confirmar<textarea name="pending" rows="2"></textarea></label></div><button>Salvar ideia</button><button type="button" onclick="cancelEdit()">Limpar formulário</button><p id="save-message" role="status"></p></form></div>'''
app=head+'<body>'+css+nav+'<div id="diagnostico" class="view">'+diag+'</div><div id="calendario" class="view active"><div id="month-live">'+monthslide(2026,11)+'</div><div class="print-only">'+monthslide(2026,12)+monthslide(2027,1)+'</div></div><div id="ideias" class="view">'+form+'</div><script id="history-data" type="application/json">'+json.dumps({str(v):json.loads((R/f'PLANEJAMENTO_MARGO_v{v:02d}.json').read_text()) for v in [3,4,5,6,7,8,9,10]},ensure_ascii=False).replace('<','\\u003c')+'</script><script id="initial-data" type="application/json">'+json.dumps(data,ensure_ascii=False).replace('<','\\u003c')+'</script><script>'+script.read_text()+'</script></body></html>'
(R/'MARGO_CALENDARIO_E_IDEIAS.html').write_text(app)
(R/'CALENDARIOS_NOVEMBRO_A_JANEIRO.pdf.html').write_text(head+'<body>'+css+months+bankpages+'</body></html>')
md='# Planejamento Margô · novembro a janeiro\n\nAtualizado em 31/10/2026. Vigente: HTML interativo e JSON v11 nesta pasta.\n\n## Direção editorial\n\nEquilibrar café e comida no feed: alternar bebidas, doces e salgados conforme o material, mantendo pessoas e experiência. Favoritos devem valorizar as escolhas reais de comida, ainda a confirmar. Favoritos: três em novembro e três em dezembro, com 9 a 12 dias entre publicações nesta proposta. Outras pautas do banco preenchem os intervalos; tudo sujeito a material e aprovação. Mocha gravado em 12/11 e Open Coffee em 21/11 alternam com Croque 07/11, red velvet 19/11 e cozinha 14/11. Amigo secreto transferido para 24/11; cozinha antecipada para 14/11. Combinação de Croque/red velvet/café transferida para 15/12. Coado continua em 10/12. Em 10/11, o cantinho vira Reel de troca de pedidos; 28/11 recebe a mesa para grupos, com foto informada pela Giovanna. O mini-vlog de domingo com horários reais passa para 16/01 como sugestão. Conceitos escolhidos pela Giovanna; captação pendente e datas sugeridas. Janeiro mantém aniversário, mini-vlog de domingo e date como propostas, sem favoritos.\n\n## Calendário de novembro a janeiro\n\n| Data | Conteúdo | Ideia do post | Formato | Estado |\n|---|---|---|---|---|\n'
for p in posts:md+='| '+' | '.join([p['date'],p['title'],p['description'],p['format'],p['status']])+' |\n'
md+='\n## Banco de ideias\n'
for i in ideas:
 md+=f'\n### {i["title"]} · {i["month"]}\n\n- Estado: {i["status"]}.\n- Origem: {i["origin"]}.\n- Abordagem: {i["angle"]}\n- Captar: {i["capture"]}\n- Pendente: {i["pending"]}\n- Reaproveitamento: {i["repeat"]}\n- Datas propostas: {", ".join(i.get("proposed_dates",[])) or "Sem data"}.\n- Fonte: {i["source"]}\n'
(R/'PLANEJAMENTO_E_BANCO_DE_IDEIAS.md').write_text(md)
print('Planejamento multimensal criado: 3 meses, 14 ideias com origem e pendências, diagnóstico preservado.')
