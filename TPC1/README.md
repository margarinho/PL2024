# Relatório da Resolução do TPC1

## Abordagem adotada
Para resolver este trabalho, foi pensado em um dicionário que, por modalidade,
organiza as linhas do dataset por faixas etárias (com intervalo de 5 anos).
A função que dá corpo ao dicionário é a função `parse`.

*exemplo:*
```
dicionary = {
    'Futebol': {
        '0-5 anos': linha do dataset,
        # ... outras faixas etárias
    }
    # ... outras modalidades desportivas
}
```

## Objectivos Cumpridos
- [x] Listagem das modalidades desportivas por ordem alfabetica
- [x] Percentagem de atletas aptos e os inaptos
- [x] Distribuicao de atletas por escalao etario (intervalo de 5 anos)

### Listagem das modalidades desportivas
Após a execução do `parse`, esta etapa corresponde apenas a um sorted da lista das chaves do dicionário.

### Percentagem de atletas aptos e os inaptos
Esta etapa recebe ajuda do parse, que retorna o número total de atletas que constam no dataset,
bem como quantos destes estão aptos, facilitando assim o cálculo das percentagens.

### Distribuicao de atletas por escalao etario (intervalo de 5 anos)

Nesta etapa, foi necessário um dicionário auxiliar que contivesse cada faixa etária associada ao número de atletas.
Depois, percorre-se o dicionário principal por modalidade para, consequentemente, percorrer as suas faixas etárias e,
por fim, contabiliza-se o número de atletas em cada uma delas, inserindo essa informação no dicionário auxiliar.
Para o resultado final, organiza-se as faixas etárias de forma crescente.

**Nota:** A modalidade dos atletas não foi levada em consideração.
