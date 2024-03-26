import sys


def age_group(age):
    start = (age // 5) * 5
    end = start + 4
    group = f"{start}-{end}"
    return group


def parse(lines, dicionary):
    capable = 0
    total = 0

    for idx, line in enumerate(lines):
        if idx == 0:
            continue
        data = line.split(',')
        age = int(data[5])
        result = data[12].strip()
        if result == 'true':
            capable += 1
        total += 1
        sport = data[8]

        group = age_group(age)

        if sport not in dicionary:
            dicionary[sport] = {}

        if group not in dicionary[sport]:
            dicionary[sport][group] = [line]
        else:
            dicionary[sport][group].append(line)

    return total, capable


def question_1(dicionary):
    return sorted(dicionary.keys())


def question_2(total, part):
    x = (part / total) * 100
    return f'{x} {100 - x}'


def sorted_ages(key):
    return int(key.split('-')[0])


def question_3(dicionary):
    result = {}
    for key in list(dicionary.keys()):
        for entry in list(dicionary[key].keys()):
            dis = len(dicionary[key][entry])
            if entry not in result:
                result[entry] = dis
            else:
                result[entry] += dis

    return dict(sorted(result.items(), key=lambda x: sorted_ages(x[0])))


def main(argv):
    dicionary = {}
    f = open(argv[1])
    total, capable = parse(f, dicionary)
    print(question_1(dicionary))
    print(question_2(total, capable))
    print(list(question_3(dicionary).items()))


if __name__ == "__main__":
    main(sys.argv)
