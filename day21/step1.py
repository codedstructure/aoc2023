from collections import defaultdict

def step(grid, markers, max_row, max_col):
    orig_markers = markers.copy()
    for pos, plot in grid.items():
        if plot == '#':
            # These will always stay at zero
            continue
        r, c = pos
        # pull bits in from neighbours
        surround = 0
        if r > 0:
            if (r - 1, c) in orig_markers:
                surround |= orig_markers[(r - 1, c)]
        if r < max_row - 2:
            if (r + 1, c) in orig_markers:
                surround |= orig_markers[(r + 1, c)]
        if c > 0:
            if (r, c - 1) in orig_markers:
                surround |= orig_markers[(r, c - 1)]
        if c < max_col - 2:
            if (r, c + 1) in orig_markers:
                surround |= orig_markers[(r, c + 1)]
        bit_pos = 1  # NOTE: not zero, since we're one step ahead
        while surround:
            if surround & 1:
                markers[pos] |= (1 << bit_pos)
            bit_pos += 1
            surround >>= 1

def main():
    start_pos = (0, 0)
    max_col = 0
    max_row = 0
    grid = {}
    with open('inputs.txt') as f:
        for row, line in enumerate(f):
            for col, ch in enumerate(line.strip()):
                if ch == 'S':
                    start_pos = (row, col)
                    ch = '.'
                grid[(row, col)] = ch
            max_col = col
        max_row = row
    markers = defaultdict(int)
    markers[start_pos] = 1

    step_target = 64
    for step_count in range(step_target):
        step(grid, markers, max_row, max_col)

    total = 0
    for plot in markers.values():
        if plot & (1 << step_target):
            total += 1
    print(total)


if __name__ == '__main__':
    main()
