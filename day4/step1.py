
def score(line):
    _, numbers = line.split(':')
    winning, selected = numbers.split('|')

    winning = set(map(int, winning.split()))

    score = 0
    for num in map(int, selected.split()):
        if num in winning:
            if score == 0:
                score = 1
            else:
                score *= 2
    return score


def main():
    with open('inputs.txt') as f:
        lines = f.readlines()

    total = 0
    for line in lines:
        total += score(line)
    print(total)


if __name__ == '__main__':
    main()
