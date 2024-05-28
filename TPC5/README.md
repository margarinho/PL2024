# Relatório da Resolução do TPC5

Este programa foi desenvolvido com o propósito de replicar o funcionamento de uma máquina de vendas.

## Estrutura do Código
O código-fonte está estruturado da seguinte forma:

1. Definição do estoque de produtos.
2. Definição de tokens usando expressões regulares.
3. Implementação de funções para análise léxica.
4. Função para encontrar um produto no estoque com base no identificador.
5. Funções auxiliares para impressão de saldo e troco.
6. Loop principal para interação com o utilizador.

## Funcionalidades Principais

- Inserção de moedas para aumentar o saldo.
- Listagem dos produtos disponíveis.
- Seleção de um produto para compra, verificando se há saldo suficiente e se o produto está disponível no estoque.
- Finalização da compra e recebimento do troco, se aplicável.

## Relatório de Testes

- **Teste de Inserção de Moedas**: Verifica que o saldo é atualizado corretamente após a inserção de moedas.
- **Teste de Listagem de Produtos**: Verifica que a lista de produtos é exibida corretamente.
- **Teste de Seleção de Produto**: Verifica que o produto é dispensado corretamente e o saldo é atualizado após a seleção de um produto.
- **Teste de Encerramento do Programa**: Verifica que o troco é exibido corretamente ao sair do programa.

## Conclusão
O simulador demonstra de forma eficaz o processo de compra em uma máquina de vendas.
