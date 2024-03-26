import re


def main(frase):
    fase_on = False

    soma = 0

    palavras = re.split(r'\s', frase, )
    #print(palavras)

    for palavra in palavras:
        #print(palavra)
        if re.search('on', palavra, re.IGNORECASE):
            fase_on = True

        if re.search('\d+', palavra) and fase_on:
            result = re.findall('[+/-]?\d+', palavra)
            for r in result:
                soma += int(r)

        if re.search('=', palavra) and fase_on:
            print(f'Soma {soma}\n')

        if re.search('off', palavra, re.IGNORECASE):
            fase_on = False
    #print (soma)


if __name__ == "__main__":
    frase = 'on cnirf 23  nsiwsj-45 = off 45'
    main(frase)
