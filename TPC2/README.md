# Relatório da Resolução do TPC2

## Abordagem adotada
Planeia-se criar uma expressão regular específica para cada tipo de expressão desejada. Ao identificar uma correspondência (match) utilizando essa expressão regular, as informações extraídas são transformadas e inseridas no formato correspondente ao original. Por defeito, o conteúdo é analisado linha a linha.

## Objectivos Cumpridos
- [x] Conversao de titulo
- [x] Conversao de negrito e italico
- [x] Conversao de listas ordenadas
- [x] Conversao de links
- [x] Conversao de imagens

### Conversao de Titulo
    exp = r'(#+) (\w*)'
O objetivo está expressao é capturar por grupos os '#' e a frase que a si se segue.

### Conversao de Negrito e Italico
    exp = r'(\*{1,2})(\w+)(\*{1,2})(.*)'
Assim como o de cima é importante fazer uma captura dos '*' as palavras que se encontram no meio e depois
guardar as palavra de se seguem à expressao enfatizada.

### Conversao de Listas Ordenadas
    exp = r'(\d\.\s)(.*)'

### Conversao de Links
    exp = r'\[([\w+\s?]+)\]\((\w+://\w+\.\w+\.\w+)\)(.*)'

Primeiro Grupo =  corresponde à descrição do link
Segundo Grupo = corresponde ao link em si

### Conversao de Imagens
    exp = r'\!\[([\w+\s?]+)\]\((\w+://\w+\.\w+\.\w+)\)(.*)'

Primeiro Grupo =  corresponde à descrição do link
Segundo Grupo = corresponde ao link em si
