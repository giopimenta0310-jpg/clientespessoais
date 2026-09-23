# Plataforma de aprovação

Plataforma para clientes aprovarem posts do Instagram antes da publicação. O cliente vê uma prévia do perfil com o grid do feed, abre cada arte (post, carrossel ou Reels) no tamanho real do Instagram, lê a legenda e **aprova**, **pede ajuste** ou **comenta**.

Visual com a identidade do studio Gio (paleta e tipografia do portfólio).

## Como funciona hoje

A versão atual (`index.html`) roda como um Artifact do Claude. Ela usa os recursos da plataforma do Claude para:

- guardar os posts, as legendas, os status e os comentários (banco de dados `db`);
- guardar as imagens e os vídeos enviados (`assets`);
- saber quem é a dona do quadro (`user`), que é a única pessoa que pode enviar e editar artes.

Por isso, **abrir este `index.html` direto no navegador ou publicar na Vercel ainda não faz ele funcionar**. A página abre em "modo prévia", sem dados. Este arquivo é o código-fonte e o backup da versão atual.

## Estrutura dos dados

- `perfil/main`: `usuario`, `nome`, `bio`, `seguidores`, `seguindo`, `avatar` (id do asset)
- `posts/<id>`: `ordem`, `tipo` (`post` | `carrossel` | `reels`), `status` (`pendente` | `aprovado` | `ajuste` | `publicado`), `legenda`, `midias` (`[{id, tipo}]`), `capa`, `comentarios` (`[{autor, texto, em}]`), `decididoEm`, `criadoEm`

## Próximo passo: versão independente (Vercel)

Para o cliente abrir um link comum, sem conta no Claude, a ideia é trocar o `db` e os `assets` por um serviço externo (por exemplo Supabase: banco e storage gratuitos) e publicar na Vercel.

## Clientes

- **Margô Cafés Especiais** (@margo), Joinville. Abertura em 10/10. Logo: `margo-logo.png`.
