from collections import defaultdict

def matches(line):
    card_num, numbers = line.split(':')
    winning, selected = numbers.split('|')

    card_num = int(card_num.split()[1])
    winning = set(map(int, winning.split()))

    match_count = 0
    for num in map(int, selected.split()):
        if num in winning:
            match_count += 1
    return (card_num, match_count)


def main():
    with open('inputs.txt') as f:
        lines = f.readlines()

    copies = defaultdict(int)
    cards = dict(map(matches, lines))
    for cn, mat in cards.items():
        copies[cn] += 1
        for i in range(mat):
            copies[cn + i + 1] += copies[cn]

    print(sum(copies.values()))


if __name__ == '__main__':
    main()
