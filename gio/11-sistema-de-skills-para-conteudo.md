# Sistema de skills para pesquisa e criação de conteúdo

## Objetivo

Montar um conjunto de skills que ajude a `gio.` a pesquisar sinais atuais, encontrar referências relevantes no nicho, entender mecanismos de conteúdos que performam e transformar esses aprendizados em conteúdo autoral, sempre subordinado ao posicionamento e à voz da marca.

## Pesquisa realizada

A pesquisa partiu do post do Reddit sobre o repositório `blacktwist/social-media-skills` e foi ampliada para coleções públicas de skills de pesquisa, tendências e criação social.

O pacote citado no Reddit é modular e cobre contexto, estratégia, criação e análise. A versão atual adicionou suporte a plataformas visuais, mas parte da arquitetura original continua mais orientada a redes baseadas em texto. Neste ambiente, já estavam disponíveis `caption-writer-sms`, `content-calendar-sms` e `content-repurposer-sms`.

A coleção `social-media-skills/skills` apresentou as melhores peças complementares para o uso pretendido: pesquisa com fontes, análise de perfis, engenharia reversa de conteúdo e execução por formato. O sistema já contava também com `trend-radar`, `trend-jacking`, `trend-opportunity-radar`, `content-autopsy`, `platform-fluency`, `voice-matching`, `read-the-room` e `hook-anatomy`.

## Skills incorporadas

- `content-research-and-sourcing`: pesquisa e verifica matéria-prima antes da criação.
- `competitor-analysis`: identifica padrões, lacunas e convenções de perfis do campo sem incentivar cópia.
- `viral-reverse-engineering`: separa o mecanismo transferível da superfície de um post viral ou acima da média.
- `reels-script`: transforma uma ideia em roteiro de Reel com gancho, retenção e captações.
- `carousel-writer`: estrutura carrosséis lâmina a lâmina.
- `story-writer`: planeja sequências de Stories com função e interação coerentes.
- `gio-social-workflow`: camada criada especificamente para a marca pessoal da Giovanna; obriga as demais skills a consultar a fonte de verdade e aplicar posicionamento, voz e dimensões editoriais.

## Skills já existentes e mantidas

- Tendências: `trend-radar`, `trend-jacking`, `trend-opportunity-radar`.
- Planejamento e produção: `content-calendar-sms`, `caption-writer-sms`, `content-repurposer-sms`.
- Linguagem e contexto: `voice-matching`, `read-the-room`, `platform-fluency`, `hook-anatomy`.
- Aprendizado: `content-autopsy`.

## Decisão de arquitetura

Não instalar coleções inteiras nem skills que prometem “viralidade” sem evidência. A instalação seletiva reduz sobreposição, conflito de instruções e recomendações genéricas.

O fluxo recomendado é:

1. carregar contexto da `gio.`;
2. pesquisar sinais atuais e fontes;
3. observar perfis e conteúdos do nicho sem copiar;
4. identificar mecanismo, ciclo e encaixe;
5. classificar a oportunidade em fazer, adaptar, observar ou descartar;
6. executar no formato adequado;
7. analisar o desempenho em série e registrar aprendizados.

## Fontes principais

- Reddit: <https://www.reddit.com/r/ClaudeAI/comments/1s2ds95/i_open_sourced_13_claude_code_skills_that_help/>
- Pacote citado: <https://github.com/blacktwist/social-media-skills>
- Coleção complementar: <https://github.com/social-media-skills/skills>
- Repositório de skills de leitura de tendências: <https://github.com/scrollmark/social-skills>

## Regra de uso

Tendência é insumo, não direção de marca. Uma oportunidade só deve virar conteúdo quando existir relação natural com repertório, processo, trabalho ou vida da Giovanna e quando a execução puder ser genuinamente autoral.
