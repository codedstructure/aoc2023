import itertools
import math

def main():
    with open('inputs.txt') as f:
        lines = f.readlines()

    lr_instrs = lines[0].strip()
    nodes = {}
    for line in lines[2:]:
        node, _, left, right = line.split()
        left = left.strip('(,')
        right = right.strip(')')
        nodes[node] = (left, right)

    camels = []
    for k in nodes:
        if k.endswith('A'):
            camels.append(k)

    counts = []
    for pos in camels:
        # Wasted time here because I didn't restart the cycle
        # from the beginning for each camel...
        for count, direction in enumerate(itertools.cycle(lr_instrs)):
            if pos.endswith('Z'):
                break
            pos = nodes[pos][0 if direction == 'L' else 1]
        counts.append(count)

    print(math.lcm(*counts))

if __name__ == '__main__':
    main()
