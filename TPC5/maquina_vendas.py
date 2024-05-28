import datetime
import re

import ply.lex as lex

stock = [
    {"cod": "A23", "nome": "água 0.5L", "quant": 8, "preco": 0.7},
    {"cod": "B45", "nome": "sabonete", "quant": 15, "preco": 1.5},
    {"cod": "C67", "nome": "pasta de dente", "quant": 10, "preco": 2.0}
]

tokens = (
    'NUMBER', 'MOEDA',
    'LISTAR', 'SELECIONAR', 'SAIR'
)

t_MOEDA = r'MOEDA.*'
t_LISTAR = r'LISTAR'
t_SELECIONAR = r'SELECIONAR.*'
t_SAIR = r'SAIR'
t_ignore = ' \t\n'


def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def match(code):
    for produto in stock:
        if produto["cod"] == code:
            return code, produto["nome"], produto['quant'], produto['preco']
    return None, None, None, None


def print_troco(saldo):
    moedas = {
        "2e": 0, "1e": 0,
        "50c": 0, "20c": 0, "10c": 0, "5c": 0, "2c": 0, "1c": 0
    }
    valor = int(saldo * 100)

    moedas['2e'] = valor // 200
    valor %= 200

    moedas['1e'] = valor // 100
    valor %= 100

    moedas['50c'] = valor // 50
    valor %= 50

    moedas['20c'] = valor // 20
    valor %= 20

    moedas['10c'] = valor // 10
    valor %= 10

    moedas['5c'] = valor // 5
    valor %= 5

    moedas['2c'] = valor // 2
    valor %= 2

    moedas['1c'] = valor

    r = []

    for m, q in moedas.items():
        if q > 0:
            r.append(f'{q}*{m}')

    if len(r) > 1:
        return ', '.join(r[:-1]) + ' e ' + r[-1]
    else:
        return r[0]


def print_saldo(saldo):
    i = int(saldo)  # Convertendo para inteiro
    d = int((saldo - i) / 0.01)
    if i > 0:
        return f'{i}e{d}c'
    else:
        return f'{d}c'


def print_listar():
    print('maq:\ncod | nome | quantidade | preço')

    print("---------------------------------")

    for produto in stock:
        cod = produto["cod"]
        nome = produto["nome"]
        quantidade = produto["quant"]
        preco = produto["preco"]

        print(f"{cod} | {nome} | {quantidade} | {preco}")


def main():
    print(f'maq: {datetime.datetime.now()}, Stock carregado, Estado atualizado.')
    print(f'maq: Bom dia. Estou disponível para atender o seu pedido.')
    saldo = 0
    on = True
    lexer = lex.lex()
    while on:
        resposta = input('>>')
        lexer.input(resposta)
        tok = lexer.token()

        if tok.type == 'MOEDA':
            result = re.split(r'\s', tok.value, )
            result.pop(0)
            result.pop(-1)
            for r in result:
                lexer.input(r)
                numero = lexer.token().value
                if re.search('e', r):
                    saldo += numero
                else:
                    saldo += numero * 0.01
            print(f'maq: Saldo = {print_saldo(saldo)}')
        elif tok.type == 'LISTAR':
            print_listar()
        elif tok.type == 'SELECIONAR':
            result = re.split(r'\s', tok.value, )
            code, nome, quant, preco = match(result.pop(1))
            if not code:
                print('maq: ERROR')
            elif quant < 0:
                print('maq: ERROR')
            elif preco > saldo:
                print('maq: Saldo insufuciente para satisfazer o seu pedido')
                print(f'maq: Saldo = {print_saldo(saldo)}; Pedido = {print_saldo(preco)}')

            else:
                print(f'maq: Pode retirar o produto dispensado "{nome}"')
                saldo -= preco
                print(f'maq: Saldo = {print_saldo(saldo)}')
        elif tok.type == 'SAIR':
            print(f'maq: Pode retirar o troco: {print_troco(saldo)}')
            print(f'maq: Até à próxima')
            on = False


if __name__ == "__main__":
    main()
