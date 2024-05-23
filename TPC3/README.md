# Relatório da Resolução do TPC3

## Abordagem adotada
Para resolver este trabalho, foi desenvolvida uma função parser que analisa a entrada token a token.
Conforme definido pelo enunciado, para o bom funcionamento deste programa era necessária a noção dos
modos `on` e `off`. A solução implementada foi a seguinte:

- Ao detetar a palavra `on`, um booleano de verificação passa a `verdadeiro`.
- Ao detetar a palavra `off`, o booleano passa a `falso`.
- As funções de *Soma* e *Resultado* dependem do valor deste booleano para funcionarem.


## Objectivos Cumpridos
- [x] Distinção do modo `on` e do modo `off`
- [x] Função de Soma só funciona no modo `on`
- [x] Função de Resultado só funciona no modo `on`


### Deteção do `on`
Para detetar a ativação do modo `on`, utilizamos a seguinte expressão regular:
    exp = r'on'

### Deteção do `off`
Para detetar a desativação do modo `off`, utilizamos a seguinte expressão regular:
    exp = r'off'

### Deteção do Número
Para a deteção de números inteiros, positivos ou negativos, utilizamos duas expressões regulares, conforme necessário:
    exp = r'\d+'
    exp = r'[+/-]?\d+'

### Deteção do Resultado `=`
Para detetar o operador de resultado `=`, utilizamos a seguinte expressão regular:
    exp = r'='
