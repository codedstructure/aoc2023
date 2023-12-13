from collections import Counter

def hand(line):
    cards, bid = line.split()
    bid = int(bid)
    ccount = Counter(list(cards))
    score_type = sorted(ccount.values(), reverse=True)
    cards = cards.replace('T', 'a').replace('J', 'b').replace('Q', 'c').replace('K', 'd').replace('A', 'e')
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
