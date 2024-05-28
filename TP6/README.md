# Exercício TP6

## Gramática

Inicio -> S Inicio | ε

S -> '?' Variavel           
    | '!' Expressao         
    | Variavel '=' Expressao  
       
Expressao -> Parcela Expressao
          | '+' Parcela
          | '-' Parcela

Parcela -> Fator Parcela
          | '*' Fator
          | '/' Fator

Fator -> '(' Expressao ')'
        | num
        | Variavel
        
Variavel -> id

