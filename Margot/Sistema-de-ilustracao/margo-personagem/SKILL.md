---
name: margo-personagem
description: "Cria e amplia o sistema de ilustrações da Margô Cafés Especiais — novas poses da personagem, cenas, objetos isolados e variantes positivas ou negativas — preservando a identidade visual aprovada. Use em pedidos que mencionem Margô/Margot, sua personagem ou ilustrações da marca; não use para fotografia ou para identidades visuais de outras marcas."
---

# Margô — personagem e sistema de ilustração

Use esta skill para manter consistente todo o universo ilustrado da Margô, com ou sem a personagem.

## Escolha o fluxo

- **Nova pose, expressão ou ação da Margô:** leia [references/character-bible.md](references/character-bible.md), [references/illustration-system.md](references/illustration-system.md) e a receita de personagem em [references/prompt-recipes.md](references/prompt-recipes.md).
- **Objeto ou elemento sem a personagem:** leia [references/illustration-system.md](references/illustration-system.md) e a receita de objetos em [references/prompt-recipes.md](references/prompt-recipes.md).
- **Versão negativa ou mudança de cor de um desenho aprovado:** não regenere a arte. Use `scripts/make_negative.py` para preservar exatamente a geometria e os recortes.
- **Reutilização de uma pose já aprovada:** copie o arquivo correspondente de `assets/approved/`; não recrie por geração.

## Regras essenciais

- Trate `assets/approved/positive/margo-em-pe.png` como a referência-mestre da personagem.
- Para novas ações, use também a pose aprovada mais próxima como referência visual.
- Preserve rosto, franja, cabelo ondulado, argolas, colar, tatuagens, roupa, proporções compactas e atitude. Mudanças de ação não autorizam redesenhar a personagem.
- A cor institucional da ilustração é vinho `#81010E`.
- Mantenha traço fino, orgânico e levemente imperfeito; formas simples; poucos detalhes internos; leitura editorial e artesanal.
- Na versão positiva, cabelo e blusa são as duas grandes massas em vinho. O restante combina branco e contornos vinho.
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
7. Quando houver versão negativa, derive-a do PNG aprovado com o script; nunca peça ao gerador para redesenhar a inversão.

## Assets aprovados

- `assets/approved/positive/`: seis poses positivas aprovadas.
- `assets/approved/negative-white/`: versões negativas brancas para fundos escuros.
- `assets/approved/negative-burgundy/`: versões negativas vinho para fundos claros.
- `assets/contact-sheets/`: pranchas para comparação rápida; não são arquivos finais transparentes.
