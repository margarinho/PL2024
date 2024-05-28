# Relatório da Resolução do TPC4

## Léxico com PLY

### Abordagem
Para este projeto, foi implementado um lexer para uma linguagem SQL simplificada usando a biblioteca PLY (Python Lex-Yacc).
Respeitando as regras da biblioteca, declarou-se palavras reservadas, operadores de comparação, identificadores e números. 

### Objectivos Cumpridos
- [x] Reconhecer Palavras Reservadas
- [x] Reconhecer Operadores de Comparação
- [x] Reconhecer Identificadores
- [ ] Distinguir os diferentes Identificadores por Atributo ou Tabela
- [x] Reconhecer Números

## Léxico Manual

### Abordagem
Inspirado nas lições teóricas sobre análise léxica e com o propósito de distinguir identificadores através de atributos ou tabelas,
foi concebido este projeto. No início, efetua-se a associação entre o tipo de token e a sua expressão regular correspondente. Posteriormente,
desenvolve-se uma expressão regular composta com base nas especificações dos tokens. Nesta fase, são definidos grupos nomeados para cada tipo de token,
utilizando a sintaxe (?P<nome_do_grupo>expressão_regular), onde nome_do_grupo representa o nome do grupo de captura e expressão_regular é a expressão
regular correspondente ao token. Todos estes grupos são então concatenados através do operador |, por meio da função join(), resultando numa única expressão 
regular composta. Em fases subsequentes, procede-se à análise das ocorrências dos tokens nesta expressão regular composta.

### Objectivos Cumpridos
- [x] Reconhecer Palavras Reservadas
- [x] Reconhecer Operadores de Comparação
- [x] Reconhecer Identificadores
- [x] Distinguir os diferentes Identificadores por Atributo ou Tabela
- [x] Reconhecer Números
