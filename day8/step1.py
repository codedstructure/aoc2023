import itertools

def main():
    with open('inputs.txt') as f:
        lines = f.readlines()

    lr_cycle = itertools.cycle(lines[0].strip())
    nodes = {}
    for line in lines[2:]:
        node, _, left, right = line.split()
        left = left.strip('(,')
        right = right.strip(')')
        nodes[node] = (left, right)

    pos = 'AAA'
    for count, direction in enumerate(lr_cycle):
        if pos == 'ZZZ':
            break
        pos = nodes[pos][0 if direction == 'L' else 1]
    print(count)

if __name__ == '__main__':
    main()
