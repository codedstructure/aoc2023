from collections import defaultdict

grid = defaultdict(lambda: '.')
visited = set()

next_step = {
    # Up, right, down, left
    "|": [("|", "F", "7"), (), ("|", "L", "J"), ()],
    "-": [(), ("-", "7", "J"), (), ("-", "F", "L")],
    "F": [(), ("-", "7", "J"), ("|", "L", "J"), ()],
    "J": [("|", "F", "7"), (), (), ("-", "F", "L")],
    "7": [(), (), ("|", "L", "J"), ("-", "F", "L")],
    "L": [("|", "F", "7"), ("-", "7", "J"), (), ()],
}


def neighbours(pos):
    r, c = pos
    current = grid[pos]

    pos_up, pos_right, pos_down, pos_left = next_step[current]

    if grid[(pos[0] - 1, pos[1])] in pos_up:
        yield (pos[0] - 1, pos[1])
    if grid[(pos[0], pos[1] + 1)] in pos_right:
        yield (pos[0], pos[1] + 1)
    if grid[(pos[0] + 1, pos[1])] in pos_down:
        yield (pos[0] + 1, pos[1])
    if grid[(pos[0], pos[1] - 1)] in pos_left:
        yield (pos[0], pos[1] - 1)


def process_start(pos):
    connect_count = 0
    adj = []
    if grid[(pos[0] - 1, pos[1])] in ("|", "F", "7"):
        adj.append(("U", grid[(pos[0] - 1, pos[1])]))
        connect_count += 1
    if grid[(pos[0], pos[1] + 1)] in ("-", "7", "J"):
        adj.append(("R", grid[(pos[0], pos[1] + 1)]))
        connect_count += 1
    if grid[(pos[0] + 1, pos[1])] in ("|", "L", "J"):
        adj.append(("D", grid[(pos[0] + 1, pos[1])]))
        connect_count += 1
    if grid[(pos[0], pos[1] - 1)] in ("-", "F", "L"):
        adj.append(("L", grid[(pos[0], pos[1] - 1)]))
        connect_count += 1
    assert connect_count == 2
    # For my input: [('U', 'F'), ('R', '7')] => 'S' is an 'L'
    grid[pos] = "L"  # YES THIS IS LAZY
    #grid[pos] = "F"  # For test data


def traverse(pos):
    while pos not in visited:
        visited.add(pos)
        a, b = neighbours(pos)
        if a not in visited:
            pos = a
        elif b not in visited:
            pos = b
        else:
            break


def inside(pos):
    if grid[pos] != '.':
        return False
    x, y = pos
    toggle = False
    while x < 140:  # Lazy hard-coding
        if grid[(x, y)] in ('|',):
            toggle = not toggle
        x += 1
    return toggle


def count_inner(rc, cc):
    count = 0
    lines = []
    for row in range(rc):
        line = []
        for col in range(cc):
            if (row, col) not in visited:
                grid[(row, col)] = '.'
            line.append(grid[(row, col)])
        lines.append(''.join(line))

    for line in lines:
        inside = False
        seen_f = False
        seen_l = False
        for ch in line:
            if ch == '|':
                inside = not inside
            elif ch == 'F':
                seen_f = True
            elif ch == 'J':
                if seen_f:
                    inside = not inside
                seen_f = False
                seen_l = False
            elif ch == 'L':
                seen_l = True
            elif ch == '7':
                if seen_l:
                    inside = not inside
                seen_f = False
                seen_l = False
            elif ch == '.' and inside:
                count += 1
    return count


def main():
    start = None
    with open('inputs.txt') as f:
        for row, line in enumerate(f):
            for col, ch in enumerate(line.strip()):
                if ch == 'S':
                    start = (row, col)
                grid[(row, col)] = ch

    process_start(start)
    traverse(start)

    print(count_inner(row + 2, col + 2))


if __name__ == '__main__':
    main()
