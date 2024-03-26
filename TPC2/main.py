import re
import sys


def headings(line):
    exp = r'(#+) (\w*)'
    result = re.match(exp, line)
    if not result:
        return
    html = f'<h{len(result.group(1))}>{str(result.group(2))}</{len(result.group(1))}>\n'
    return html


def emphasis(line):
    exp = r'(\*{1,2})(\w+)(\*{1,2})(.*)'
    result = re.match(exp, line)
    igual = len(result.group(1)) != len(result.group(3))

    if not result or igual or len(result.group(1)) > 2:
        return

    if len(result.group(1)) == 1:
        return f'<i>{str(result.group(2))}</i>{str(result.group(4))}\n'
    if len(result.group(1)) == 2:
        return f'<b>{str(result.group(2))}</b>{str(result.group(4))}\n'


def ordered_list(line):
    exp = r'(\d\.\s)(.*)'
    result = re.match(exp, line)

    if not result:
        return

    html = f'\t<li>{result.group(2)}</li>\n'

    return html


def links(line):
    exp = r'\[([\w+\s?]+)\]\((\w+://\w+\.\w+\.\w+)\)(.*)'
    result = re.match(exp, line)

    if not result:
        return

    html = f'<a href="{str(result.group(1))}">{str(result.group(2))}</a>{str(result.group(3))}\n'
    return html


def images(line):
    exp = r'\!\[([\w+\s?]+)\]\((\w+://\w+\.\w+\.\w+)\)(.*)'
    result = re.match(exp, line)
    if not result:
        return

    html = f'<img src="{str(result.group(1))}" alt="{str(result.group(2))}"/>{str(result.group(3))}\n'
    return html


def main(argv):
    r = ""
    lista = False
    with open(argv, 'r') as md:
        for line in md:

            if re.search('\d\.', line) is not None:

                if not lista:
                    r += '<ol>\n'
                    lista = True
                result = ordered_list(line)
                if result:
                    r += result

            elif re.search('#', line):
                result = headings(line)
                if result is not None:
                    r += result

            elif re.search('\*', line):
                result = emphasis(line)
                if result:
                    r += result

            elif re.search(r'!\[', line):
                result = images(line)
                if result:
                    r += result

            elif re.search('\[', line):
                result = links(line)
                if result:
                    r += result

            else:
                if lista:
                    r += '</ol>\n'
                    lista = False
                else:
                    r += line

    with open('out', 'w') as wf:
        wf.write(r)


if __name__ == "__main__":
    main(sys.argv[1])
