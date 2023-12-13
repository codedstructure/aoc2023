from collections import defaultdict
import re

class Game:
    def __init__(self, spec):
        self.id = int(re.match("Game (\d+):", spec).group(1))
        draws = spec.split(':', 1)[1].split(';')

        min_cubes = defaultdict(int)
        for draw in draws:
            for col_draw in draw.split(','):
                count, col = col_draw.strip().split()
                count = int(count)
                if min_cubes[col] < count:
                    min_cubes[col] = count
        self.min_cubes = min_cubes

    def power(self):
        mult = 1
        for _, count in self.min_cubes.items():
            mult *= count
        return mult


def main():
    total = 0
    with open('inputs.txt') as f:
        for line in f:
            g = Game(line)
            total += g.power()
    print(total)


if __name__ == '__main__':
    main()
