# Pesquisa de skills para social media — BC na Cozinha

**Data:** 01/10/2026  
**Objetivo:** montar um conjunto de skills para pesquisar tendencias e referencias, aprender com conteudos fortes e criar materiais alinhados a estrategia da BC na Cozinha.

## Decisao

Nao instalar pacotes inteiros nem duplicar funcoes. Usar uma camada propria da BC como fonte de verdade e combinar apenas especialistas para cada etapa.

## O que veio do Reddit

O post apresenta skills modulares para contexto de marca, estrategia, calendario, redacao, reaproveitamento e analise. A ideia mais valiosa e correta para a BC e separar o contexto da marca da habilidade de formato: a voz, o publico e os limites operacionais devem ser lidos antes da criacao.

O conjunto original nasceu com foco em plataformas de texto e depois adicionou suporte a formatos visuais. Para a BC, Instagram, Reels e Stories sao centrais; por isso, as skills do post sao usadas apenas onde sao fortes e complementadas por ferramentas especificas de Instagram e pesquisa atual.

Fonte: https://www.reddit.com/r/ClaudeAI/comments/1s2ds95/i_open_sourced_13_claude_code_skills_that_help/

## Stack ativa

### Camada da marca

- `bc-social-workflow`: fonte de verdade, criterios de aderencia, voz, jornada, pilares e limites operacionais.

### Descoberta e validacao

- `trend-opportunity-radar`: pesquisa delimitada e baseada em evidencias por plataforma.
- `trend-radar`: avalia relevancia, ciclo e timing de uma tendencia.
- `trend-jacking`: testa encaixe, seguranca e timing antes de adaptar.
- `content-research-and-sourcing`: verifica fontes e fatos que sustentam conteudos.
- `competitor-analysis`: compara contas e identifica lacunas sem copiar.
- `viral-reverse-engineering`: analisa um post forte e extrai o mecanismo transferivel.
- `read-the-room`: interpreta comentarios, linguagem e subtexto do publico.

### Criacao

- `hook-anatomy`: cria e avalia ganchos.
- `reels-script`: estrutura Reels de Instagram.
- `carousel-writer`: organiza carrosseis lamina a lamina.
- `story-writer`: cria sequencias de Stories.
- `caption-writer-sms`: escreve legendas para conteudo visual.
- `content-repurposer-sms`: transforma uma captacao em varias pecas com funcoes diferentes.
- `content-calendar-sms`: distribui conteudos por objetivo e cadencia.
- `platform-fluency`: aplica convencoes atuais de cada plataforma.

### Aprendizado

- `content-autopsy`: compara desempenho e transforma resultados em hipoteses de teste.
- `voice-matching`: ajuda a manter consistencia quando houver amostras reais suficientes da voz da Bruna.

## Opcoes pesquisadas e nao incorporadas agora

### ScrapeCreators social-media-research-skills

Tem boas funcoes para encontrar outliers, minerar comentarios, pesquisar concorrentes e tendencias em varias plataformas. Exige chave de API da ScrapeCreators. E uma expansao util se a BC precisar de coleta em escala, mas nao deve ser dependencia do fluxo atual.

Fonte: https://github.com/ScrapeCreators/social-media-research-skills

### Awesome Social Media Skills

Bom catalogo para descoberta, mas e uma colecao ampla. Instalar itens individualmente sem uma lacuna clara aumentaria sobreposicao.

Fonte: https://github.com/replynodes/awesome-social-media-skills

### Social Media Skills (106 skills)

Colecao robusta e compativel com agentes, com cobertura de pesquisa, estrategia, criacao, publicacao e analise. Foram selecionadas apenas as funcoes necessarias para a BC; o pacote completo criaria duplicacao e maior chance de conflito.

Fonte: https://github.com/social-media-skills/skills

## Fluxo recomendado

1. Comecar pela pergunta de negocio e pela funcao do conteudo.
2. Pesquisar sinais atuais em um nicho e plataforma definidos.
3. Filtrar por aderencia a BC, seguranca, timing e capacidade operacional.
4. Extrair o mecanismo da referencia, nunca copiar a superficie.
5. Criar no formato adequado e revisar pela voz e pelos pilares da BC.
6. Publicar apenas com informacoes comerciais confirmadas.
7. Comparar resultados por funcao e alimentar o proximo ciclo.

## Criterio de sucesso

O sistema nao busca "viral por viral". Uma oportunidade e boa quando aumenta descoberta, compreensao, desejo, confianca ou compra entre pessoas com afinidade e potencial local, sem descaracterizar a marca nem ultrapassar a capacidade real.
