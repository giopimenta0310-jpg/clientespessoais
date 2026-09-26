---
name: margo-personagem
description: "Cria e amplia o sistema de ilustrações da Margô Cafés Especiais a partir da personagem simples derivada do mural e da paleta vigente no Figma. Use em pedidos que mencionem Margô/Margot, sua personagem ou ilustrações da marca; não use as explorações antigas em vinho como referência principal."
---

# Margô — personagem e sistema de ilustração

Use esta skill para manter consistente todo o universo ilustrado da Margô, com ou sem a personagem.

> **Decisão vigente — 26/09/2026:** a personagem oficial é a versão simples derivada do mural, localizada em `../../Assets/Personagem/`. A personagem detalhada em vinho preservada dentro deste diretório é uma exploração legada e não deve orientar novas artes.

## Escolha o fluxo

- **Nova pose, expressão ou ação da Margô:** leia [references/character-bible.md](references/character-bible.md), [references/illustration-system.md](references/illustration-system.md) e a receita de personagem em [references/prompt-recipes.md](references/prompt-recipes.md).
- **Objeto ou elemento sem a personagem:** leia [references/illustration-system.md](references/illustration-system.md) e a receita de objetos em [references/prompt-recipes.md](references/prompt-recipes.md).
- **Versão negativa ou mudança de cor de um desenho aprovado:** não regenere a arte. Use `scripts/make_negative.py` para preservar exatamente a geometria e os recortes.
- **Reutilização de uma pose já aprovada:** copie o arquivo correspondente de `../../Assets/Personagem/`; não recrie por geração.

## Regras essenciais

- Trate `../../Assets/Personagem/margo-personagem-principal-v01.png` como a referência-mestre da personagem.
- Para novas ações, use também a pose aprovada mais próxima como referência visual.
- Preserve cabelo curto, óculos escuros redondos, silhueta simples, blusa ampla, calça larga e proporções compactas. Mudanças de ação não autorizam redesenhar a personagem.
- Use a paleta derivada do mural e aplicada no Figma: preto, off-white/creme, rosa e verde, com roxo e magenta quando a composição pedir.
- Mantenha traço preto simples, orgânico e levemente imperfeito; poucas linhas internas; leitura ingênua, artesanal e expressiva.
- Use preenchimentos pontuais, especialmente preto/off-white e acentos rosa. Evite recuperar cabelo longo, tatuagens, argolas e detalhamento da exploração antiga.
- Evite realismo, anatomia detalhada, pernas alongadas, aparência de modelo de moda, gradientes, volume 3D, iluminação, brilho, halo, sombra projetada e fundos inventados.
- Por padrão, entregue PNG de alta resolução com transparência real fora da arte.
- Não inclua texto, logotipo ou cenário completo sem pedido explícito.

## Fluxo de produção

1. Inspecione a referência-mestre e apenas os assets relevantes para o pedido.
2. Classifique cada imagem de entrada como alvo de edição, referência de identidade ou referência de estilo.
3. Para arte nova, use geração/edição de imagem preservando agressivamente as invariantes da personagem e do sistema.
4. Faça uma alteração conceitual por iteração quando estiver refinando uma pose.
5. Valide identidade, proporção, preenchimentos, precisão dos objetos e ausência de fundo/halo.
6. Salve de forma não destrutiva com nome descritivo e versionado.
7. Para variações de cor, use as aplicações existentes no Figma como referência e preserve a geometria aprovada.

## Assets vigentes

- `../../Assets/Personagem/`: personagem oficial e poses aprovadas.
- `../../Assets/Elementos/`: objetos no universo visual vigente.
- `../../Assets/Obra-com-personagens/`: aplicações sobre fotografias da obra.
- `assets/approved/` e `assets/contact-sheets/`: explorações legadas preservadas apenas como histórico; não reutilizar como fonte principal.
