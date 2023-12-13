
galaxies = {}

def main():
    lines = []
    with open('inputs.txt') as f:
        for line in f:
            line = line.strip()
            lines.append(line)
            if not line.count('#'):
                lines.append(line)

    # transpose
    lines_t = [''.join(ln) for ln in list(zip(*lines))]

    lines = []
    for line in lines_t:
        lines.append(line)
        if not line.count('#'):
            lines.append(line)

    # re-transpose; unnecessary but makes checking against test data easier
    lines = [''.join(ln) for ln in list(zip(*lines))]

    gidx = 0
    for row, line in enumerate(lines):
        for col, ch in enumerate(line):
            if ch == '#':
                galaxies[gidx] = (row, col)
                gidx += 1

    total = 0
    for i in range(gidx):
        for j in range(gidx):
            i_r, i_c = galaxies[i]
            j_r, j_c = galaxies[j]
            total += abs(j_r - i_r) + abs(j_c - i_c)
    # rather than avoiding b->a if we've already seen a->b, just total the lot
    # and halve it.
    print(total // 2)


if __name__ == '__main__':
    main()
