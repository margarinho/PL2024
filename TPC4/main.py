import ply.lex as lex

tokens = (
    'NUMBER',
    'MAIOR', 'MENOR', 'EQUAL',
    'SELECT', 'VIRGULA', 'FROM', 'WHERE',
    'ATRIBUTO'

)

t_SELECT = r'Select'
t_FROM = r'From'
t_WHERE = r'Where'
t_VIRGULA = r','
t_MAIOR = r'>'
t_MENOR = r'<'
t_EQUAL = r'='
t_ATRIBUTO = r'\w+'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)


t_ignore = ' \t\n'

lexer = lex.lex()

data = '''
Select id, nome, salario From empregados Where salario >= 820
'''

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)



