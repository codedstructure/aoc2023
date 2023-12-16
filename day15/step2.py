import re
from collections import defaultdict

boxes = defaultdict(list)

def ihash(inst):
    h = 0
    for ch in inst:
        h = ((h + ord(ch)) * 17) % 256
    return h


def main():
    with open('inputs.txt') as f:
        instructions = f.read().strip().split(',')

    for inst in instructions:
        label, op = re.match('([a-z]+)(-|=\d+)', inst).groups()
        box = ihash(label)

        # I'm not pleased with this code, but it works for the given
        # scale of data.
        if op[0] == '=':
            lens = int(op[1:])
            exist = [(lbl, idx) for (idx, (lbl, _)) in enumerate(boxes[box]) if lbl == label]
            if exist:
                lbl, idx = exist[0]
                boxes[box][idx] = (label, lens)
            else:
                boxes[box].append((label, lens))
        else:
            exist = [(lbl, idx) for (idx, (lbl, _)) in enumerate(boxes[box]) if lbl == label]
            if exist:
                lbl, idx = exist[0]
                del boxes[box][idx]

    power = 0
    for box, lenses in boxes.items():
        for slot, (_, lens) in enumerate(lenses, 1):
            power += (1 + box) * slot * lens
    print(power)




if __name__ == '__main__':
    main()
