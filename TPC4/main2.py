import re

data = 'Select id, nome, salario From empregados Where salario >= 820'


def tokenize():
    token_specification = [
        ('NUM', r'\d+'),
        ('IGUAL', r'='),
        ('MAIOR', r'>'),
        ('MENOR', r'<'),
        ('SELECT', r'Select'),
        ('FROM', r'From'),
        ('WHERE', r'Where'),
        ('VIRGULA', r','),
        ('ATRIBUTO', r'\w+'),
        ('ERRO', r'.'),
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    reconhecidos = []
    linha = 1
    fase = 0
    t = None
    mo = re.finditer(tok_regex, data)

    for m in mo:
        dic = m.groupdict()
        if dic['NUM'] is not None:
            t = ("NUM", int(dic['NUM']), linha, m.span())
        elif dic['IGUAL'] is not None:
            t = ("IGUAL", dic['IGUAL'], linha, m.span())
        elif dic['MAIOR'] is not None:
            t = ("MAIOR", dic['MAIOR'], linha, m.span())
        elif dic['MENOR'] is not None:
            t = ("MENOR", dic['MENOR'], linha, m.span())
        elif dic['SELECT'] is not None:
            t = ("SELECT", dic['SELECT'], linha, m.span())
        elif dic['FROM'] is not None:
            fase = 1
            t = ("FROM", dic['FROM'], linha, m.span())
        elif dic['WHERE'] is not None:
            fase = 2
            t = ("WHERE", dic['WHERE'], linha, m.span())
        elif dic['VIRGULA'] is not None:
            t = ("VIRGULA", dic['VIRGULA'], linha, m.span())
        elif dic['ATRIBUTO'] is not None:
            if fase == 0:
                t = ("COLUMN", dic['ATRIBUTO'], linha, m.span())
            elif fase == 1:
                t = ("TABLE", dic['ATRIBUTO'], linha, m.span())
            elif fase == 2:
                t = ("CONDITION", dic['ATRIBUTO'], linha, m.span())
        else:
            t = ("ERRO", m.group(), linha, m.span())
        if t:
            reconhecidos.append(t)
    return reconhecidos


print(tokenize())
