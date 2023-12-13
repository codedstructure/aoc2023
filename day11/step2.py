
galaxies = {}

def main():
    exp_rows = []
    exp_cols = []

    lines = []
    with open('inputs.txt') as f:
        for idx, line in enumerate(f):
            line = line.strip()
            lines.append(line)
            if not line.count('#'):
                exp_rows.append(idx)

    # transpose
    lines_t = [''.join(ln) for ln in list(zip(*lines))]

    lines = []
    for idx, line in enumerate(lines_t):
        lines.append(line)
        if not line.count('#'):
            exp_cols.append(idx)

    # re-transpose; unnecessary but makes checking against test data easier
    lines = [''.join(ln) for ln in list(zip(*lines))]

    # -1 because we've already got a single 'space' in our data, this is how
    # many more we need.
    EXPANSION = 1_000_000 - 1
    gidx = 0
    for row, line in enumerate(lines):
        extra_rows = len(list(filter(lambda x: x < row, exp_rows)))
        for col, ch in enumerate(line):
            extra_cols = len(list(filter(lambda x: x < col, exp_cols)))
            if ch == '#':
                # print(f"{gidx}: {row}+{extra_rows}, {col}+{extra_cols}")
                galaxies[gidx] = (row + (extra_rows * EXPANSION), col + (extra_cols * EXPANSION))
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
