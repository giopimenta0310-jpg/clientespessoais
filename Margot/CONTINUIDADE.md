# Continuar a Margô em outro computador

## Começar pelo que está vigente

1. Abra `CONTEXTO_ATUAL.md`.
2. Leia `Entregaveis/CALENDARIO_ATUALIZADO_25_A_30_OUTUBRO.md` e `Entregaveis/OPEN_COFFEE_E_OFICINA_CROCHE_COPIES_ATUALIZADAS.md`. As copies de 19/10 permanecem em `Entregaveis/Replanejamento-19-outubro/CALENDARIO_E_COPIES_APROVADAS.md`, com datas posteriores substituídas pelo calendário atualizado.
3. Consulte `Conversa/continuacao-2026-10.md` para entender as decisões. É uma síntese, não uma transcrição literal de todas as mensagens.
4. Para conteúdo de Instagram, leia `Sistema-de-conteudo/margo-social-workflow/SKILL.md` e a referência de marca que ele indica.

## Clonar e sincronizar

```sh
git clone https://github.com/giopimenta0310-jpg/clientespessoais.git
cd clientespessoais
git pull --ff-only
```

Abra a subpasta `Margot/` no VS Code ou o arquivo `Margot/Margô.code-workspace`. O nome da pasta no repositório é **Margot**; a pasta de trabalho anterior deste Mac chamava-se **Margô**.

Antes de trocar de computador, confira `git status`, revise as alterações, faça commit e envie com `git push`. No outro computador, faça `git pull --ff-only` antes de editar. Se houver mudanças locais, preserve-as antes de puxar; não use comandos de descarte ou force push para resolver uma divergência automaticamente.

Clonar um repositório público não exige autenticação. Enviar alterações exige uma conta autorizada no GitHub, pelo Git do computador ou pelo conector GitHub do Codex. Conexões, credenciais e skills instaladas globalmente não são transportadas pelo clone.

## O que o Git guarda

- Contexto da marca, histórico de decisões, calendários, copies, documentos editáveis e PDFs.
- Biblioteca de elementos e personagens, referências e índices dos materiais.
- Código-fonte do motion, imagens utilizadas, sons, `package.json` e `package-lock.json`.
- Inventário e folhas de contato da pasta de captação `17-10`, para orientar seleção e edição.

O estado aprovado está em Markdown/JSON além de PDF/DOCX. Isso permite ler e editar o projeto sem depender de uma aplicação específica.

## O que precisa ser transferido separadamente

Arquivos brutos de câmera e exports grandes não entram no Git. Para editar o material em outra máquina, leve por Drive, disco ou outro armazenamento:

- **Pasta `17-10` completa**, mantendo subpastas e nomes: 78 HEIC e 14 MOV. Origem neste Mac: `/Users/giovannapimenta/Downloads/17-10`.
- **Vídeo Inauguração - Margô.mov**, finalizado por Giovanna. Origem informada: Downloads deste Mac; não é parte do código Remotion.
- **Exports em `Motion/whatsapp-inauguracao/out/`**, caso queira reutilizar os arquivos renderizados prontos em vez de renderizar novamente. Os fontes e assets necessários ficam no Git.
- Novas captações realizadas depois deste registro.

As folhas de contato são prévias, não substituem os originais em resolução completa. Nenhuma pasta de Drive para esses brutos foi confirmada. O caminho de Downloads é apenas uma referência local; escolha o novo caminho no computador de destino.

## Motion / Remotion

Instale Node.js 22 e npm. Na pasta `Margot/Motion/whatsapp-inauguracao`:

```sh
npm ci
npm run check
npm run studio
```

Composições: `WhatsApp-Motion` (primeiro break, 20 s) e `WhatsApp-Futuro` (retorno e desejos, 15 s), ambas 1080 × 1920, 30 fps. As capas são imagens de encaixe para a edição externa; o depoimento final não está embutido nesses prints. Consulte o README do motion para histórico e props.

Não dependa da instalação temporária de Node em `/tmp` usada no Mac original. `node_modules`, navegador baixado pelo Remotion e renders são reconstruídos/gerados localmente.

## Regerar documentos

Os scripts Ruby dos calendários usam o DOCX de referência versionado em `Entregaveis/`. O documento vigente pode ser regenerado com:

```sh
ruby Entregaveis/Replanejamento-19-outubro/gerar_aprovado.rb
```

Execute a partir de `Margot/`. O script gera DOCX, HTML, Markdown e JSON. O PDF é uma exportação do HTML em A4 pelo navegador; já existe uma versão pronta no repositório. Os scripts v02–v04 são históricos e não devem substituir a v05 aprovada.

## Limites do registro

Não presumir que uma arte foi publicada porque a copy foi aprovada. Não tratar propostas antigas como datas vigentes. Não reconstruir a personagem a partir das explorações vinho; usar a versão do mural. Ao retomar, atualizar este registro e o contexto com decisões novas.
