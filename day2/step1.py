from collections import defaultdict
import re

class Game:
    def __init__(self, spec):
        self.id = int(re.match("Game (\d+):", spec).group(1))
        draws = spec.split(':', 1)[1].split(';')

        valid = True
        for draw in draws:
            max_draw = defaultdict(int)
            for col_draw in draw.split(','):
                count, col = col_draw.strip().split()
                count = int(count)
                if max_draw[col] < count:
                    max_draw[col] = count
            if max_draw['red'] > 12:
                valid = False
            if max_draw['green'] > 13:
                valid = False
            if max_draw['blue'] > 14:
                valid = False
        self.valid = valid


def main():
    total = 0
    with open('inputs.txt') as f:
        for line in f:
            g = Game(line)
            if g.valid:
                total += g.id
    print(total)


if __name__ == '__main__':
    main()
