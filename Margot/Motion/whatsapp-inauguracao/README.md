# WhatsApp da Margô — direção visual 01

## Estado vigente — 19/10/2026

Projeto animado com duas composições: `WhatsApp-Motion` (20 s) e `WhatsApp-Futuro` (15 s), ambas 1080 × 1920, 30 fps. Código, imagens de apoio e sons estão versionados. Instalar Node.js 22, executar `npm ci`, `npm run check` e `npm run studio`. As capas reais já foram aplicadas; a montagem do vídeo final de depoimentos é externa ao projeto. Giovanna informou que o vídeo de inauguração foi finalizado em 16/10.

Os renders locais em `out/` e as dependências não entram no Git. Para continuar em outro computador, leia [CONTINUIDADE.md](../../CONTINUIDADE.md). O restante deste arquivo preserva as etapas históricas de construção; frases como “nenhuma animação produzida” ou capas “provisórias” devem ser lidas na ordem do histórico, não como o estado atual.

Etapa atual: quatro frames estáticos para aprovação. Nenhuma animação, áudio ou MP4 produzido.

- `frames/storyboard.png`: prancha dos quatro momentos.
- `frames/01-wallpaper.png` a `04-video-recebido.png`: telas individuais 1080 × 1920.
- `public/wallpaper-margo.png`: wallpaper sem interface.
- `public/avatar-margo.png`: foto de perfil ilustrada.
- `src/index.tsx` e `src/style.css`: construção editável das telas em Remotion.

## Direção

Telefone da Margô, durante a inauguração, sábado 10/10/2026, 16:42. Contato: `amiga <3`. Mensagens enviadas à direita, respostas à esquerda. Avatar da Margô junto ao grupo de mensagens enviadas: adaptação intencional, não recurso nativo do WhatsApp. Avatar da amiga representado provisoriamente por coração, sem inventar uma pessoa real. A tela inicial é uma direção estilizada com acesso visual ao WhatsApp. A capa do vídeo é uma fotografia provisória do acervo; substituir pelo primeiro frame da edição final.

Na animação futura: chegada das mensagens, indicação de digitação, toque no play e expansão do vídeo à tela cheia. Ritmo sugerido 12–15 segundos, a definir após aprovação. Ainda falta o vídeo final para fechar a passagem.

## Abrir

Com Node disponível: `npm install` e `npm run studio`.

Nesta sessão foi usado Node oficial 22.23.3 extraído em `/tmp/node-v22.23.3-darwin-x64`, sem instalação global. Esse caminho é temporário. Dependências locais fixadas no package-lock. Remotion 4.0.535. A prévia local foi iniciada em http://localhost:3000.

## Imagens e prompts

Wallpaper e avatar criados com a ferramenta de imagem integrada, sem API/CLI. Interface e texto construídos em código, não gerados na imagem.

Prompt wallpaper: “Aesthetic cool illustrated iPhone wallpaper, portrait 9:16. Warm ivory cream background, lots of empty space across top65% and center for clock/apps. Lower right small espresso cup viewed from above, sage #A3AD82 saucer/cup, organic black mural outlines, pink #FFADC9 accent. One flowing steam line turns into a pink flower. Partial sage vinyl record at bottom left. Restrained flat illustration. No character, logos, letters, UI, phone frame or watermark.”

Prompt avatar: “Square head-and-shoulders avatar of official Margô from master reference: short rounded black bob, round black sunglasses, small friendly smile, cream crewneck loose shirt, sparse organic black outlines. Sage green #A3AD82 background, soft pink #FFADC9 circle behind head. Simple flat color, readable tiny; no letters, logo, border or burgundy variant.”

## Revisão 02

Tela bloqueada com notificação e atalhos de lanterna/câmera; removido acesso fictício central. Nova amiga ilustrada no cabeçalho. Mensagem de vídeo com thumbnail 9:16 e conversa deslocada para simular rolagem; composição e futura saída permanecem 1080×1920. Arquivos revisados com sufixo `-v02`. Nenhum MP4 gerado.

Avatar amiga criado com ferramenta integrada: nova personagem fictícia no mesmo estilo de traço da Margô, cabelo cacheado castanho-avermelhado, presilha verde, olhos visíveis sem óculos, pele morena e camiseta verde, fundo rosa com círculo creme; poucos detalhes, formas planas, sem texto.

## Motion 01 — 20 segundos, 30 fps, 1080×1920

Composição `WhatsApp-Motion` em http://localhost:3000/WhatsApp-Motion.

- 0–2,1 s: notificação e toque para entrar na conversa.
- 2,3–8,65 s: três mensagens digitadas, com teclado e envio.
- 9,05–12,15 s: indicação de digitação e respostas.
- 14 s: vídeo recebido em 9:16, com rolagem.
- 16,8 s: toque no play.
- 17–18,05 s: expansão contínua até tela cheia.
- Até 20 s: ponto de entrada para edição final; por enquanto fotografia estática provisória.

`videoSrc` vazio mantém a fotografia. Para integrar o vídeo, colocar um arquivo em `public/` e indicar seu caminho relativo em `videoSrc` nas props da composição. Sons originais sintetizados nesta sessão (notificação, teclas, envio, recebimento, toque e whoosh), sem gravações externas. Sem música. Os PNGs `motion-*.png` verificam os estados de digitação e vídeo. TypeScript validado. MP4 não exportado nesta etapa.

## Motion 02 — conversa contínua

A amiga envia `ok` na notificação e a mesma mensagem abre o histórico. Notificação entra no momento do som. Cada envio respeita: digitação completa, pressão no botão, limpeza do campo, balão após 160 ms, um tique, entrega e leitura. Teclado entra e sai suavemente; rolagem acompanha a terceira mensagem. A amiga digita em intervalos antes de cada resposta. Conferidos os frames antes e depois do envio e o vídeo vertical. Mesma composição `WhatsApp-Motion`, 20 s em 1080×1920.

## Revisão de abertura e histórico

Inserida mensagem anterior enviada pela Margô: “chega cedo daí amg” às 16:40, antes do “ok” da amiga. Removidos o zoom e a dissolução da abertura; agora a janela do chat se expande a partir da região da notificação após o toque. Ajustada a rolagem para compensar a linha nova no histórico. Demais tempos e sons preservados. TypeScript e frames de abertura/histórico conferidos.

## Entrada para break na edição

Tela do celular sobe de fora do quadro em 0,38 s, sobre fundo transparente. A composição deve ser inserida sobre o vídeo anterior; exportação futura precisa preservar alpha ou receber o trecho anterior como camada. O print do depoimento enviado no chat (homem de óculos/camisa cinza na varanda) ainda não está disponível como arquivo local; não foi substituído por uma recriação. A capa antiga continua até receber o arquivo. Não usar a capa antiga como versão final.

## Capa real do depoimento aplicada

Arquivo enviado pela usuária `Captura de Tela 2026-10-16 às 18.25.24.png`, copiado integralmente para `public/capa-depoimento.png`. Aplicado no vídeo recebido e na expansão da composição `WhatsApp-Motion`. Permanece uma imagem estática para o encaixe manual do vídeo. Conferidos os frames 470 e 550. A pendência de recebimento da capa registrada acima está resolvida.

## Segundo motion — WhatsApp-Futuro

Composição independente, 15 segundos, 30fps, 1080×1920. Entrada parte do print `saida-depoimentos.png` em tela cheia e o recolhe para a mensagem recebida. A Margô reage com as falas aprovadas; a amiga introduz a pergunta sobre os desejos para o futuro da casa. Digitação, teclado, confirmação de envio, sons e zooms suaves. Novo vídeo aos 11,8s; play aos 13,4s e expansão até 14,25s. `nextPoster` é a capa do bloco seguinte, provisoriamente o mesmo print da saída. Substituir quando a usuária enviar a próxima capa. Primeiro motion preservado. Sem exportação de MP4. Frames de leitura conferidos e TypeScript validado.

## Continuidade e capa dos desejos

Histórico completo do primeiro motion incluído no segundo (chega cedo, ok, perguntas da Margô e respostas da amiga), com rolagem natural para as mensagens mais recentes. Primeiro vídeo mantém sua capa original `capa-depoimento.png`; `saida-depoimentos.png` representa apenas seu frame final na entrada do segundo motion. Vídeo dos desejos usa agora a nova captura das 18.57.33, copiada para `public/capa-desejos.png`, tanto na mensagem quanto na expansão para tela cheia. Props padrão atualizadas. TypeScript e frames conferidos.
