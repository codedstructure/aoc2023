from collections import Counter

def hand(line):
    cards, bid = line.split()
    bid = int(bid)

    jcount = cards.count('J')
    ccount = Counter(list(cards))
    if 'J' in ccount:
        del ccount['J']
    score_type = sorted(ccount.values(), reverse=True)

    if score_type:
        score_type[0] += jcount
    else:
        score_type = [jcount]

    cards = cards.replace('T', 'a').replace('J', '1').replace('Q', 'c').replace('K', 'd').replace('A', 'e')
    return score_type, cards, bid


def main():
    hands = []
    with open('inputs.txt') as f:
        for line in f:
            hands.append(hand(line))
    hands = sorted(hands)
    total = 0
    for idx, (_, _, bid) in enumerate(hands, 1):
        total += idx * bid
    print(total)


if __name__ == '__main__':
    main()
