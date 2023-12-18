from collections import defaultdict, deque

# Here pos is x, y (rather than row, col)

def steps(pos, dir, count):
    for _ in range(count):
        if dir == 'U':
            pos = (pos[0], pos[1] - 1)
        elif dir == 'D':
            pos = (pos[0], pos[1] + 1)
        elif dir == 'L':
            pos = (pos[0] - 1, pos[1])
        elif dir == 'R':
            pos = (pos[0] + 1, pos[1])
        yield pos


def display(grid, min_x, max_x, min_y, max_y):
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x,y) in grid:
                print('#', end='')
            else:
                print('.', end='')
        print()

def find_inside_point(grid, min_x, max_x, min_y, max_y):
    # BROKEN: doesn't account for horizontal boundary edges
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in grid:
                # only want an 'inside' point, not one on the boundary
                continue
            # determine winding number.
            wc = 0
            for pos_x in range(x, max_x + 1):
                if (pos_x, y) in grid:
                    wc += 1
            if wc % 2:
                return (x, y)

# recursive version, fails for large grid.
def floodfill(grid, start, min_x, max_x, min_y, max_y):
    x, y = start
    if x < min_x or x > max_x or y < min_y or y > max_y:
        return
    grid[start] = 'x'
    if (x + 1, y) not in grid:
        floodfill(grid, (x + 1, y), min_x, max_x, min_y, max_y)
    if (x - 1, y) not in grid:
        floodfill(grid, (x - 1, y), min_x, max_x, min_y, max_y)
    if (x, y + 1) not in grid:
        floodfill(grid, (x, y + 1), min_x, max_x, min_y, max_y)
    if (x, y - 1) not in grid:
        floodfill(grid, (x, y - 1), min_x, max_x, min_y, max_y)

# Adapted from https://playandlearntocode.com/article/flood-fill-algorithm-in-python
def floodfill_iter(grid, start, min_x, max_x, min_y, max_y):
    x, y = start
    if x < min_x or x > max_x or y < min_y or y > max_y:
        return

    if start in grid:
        return

    def worth_visit(p):
        if x < min_x or x > max_x or y < min_y or y > max_y:
            return False
        return p not in grid

    q = deque()
    q.append(start)

    while len(q) > 0:
        (x, y) = q.popleft()

        if worth_visit((x + 1, y)):
            grid[(x + 1, y)] = '#'
            q.append((x + 1, y))

        if worth_visit((x - 1, y)):
            grid[(x - 1, y)] = '#'
            q.append((x - 1, y))

        if worth_visit((x, y + 1)):
            grid[(x, y + 1)] = '#'
            q.append((x, y + 1))

        if worth_visit((x, y - 1)):
            grid[(x, y - 1)] = '#'
            q.append((x, y - 1))

def main():
    pos = (0, 0)
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    grid = defaultdict(str)
    with open('inputs.txt') as f:
        for line in f:
            dir, length, col = line.split()
            length = int(length)
            for step in steps(pos, dir, length):
                pos = step
                x, y = pos
                if x < min_x:
                    min_x = x
                if y < min_y:
                    min_y = y
                if x > max_x:
                    max_x = x
                if y > max_y:
                    max_y = y
                grid[pos] = col

    #display(grid, min_x, max_x, min_y, max_y)
    inside = find_inside_point(grid, min_x, max_x, min_y, max_y)
    inside = (10, 0)  # By inspection with display()
    floodfill_iter(grid, inside, min_x, max_x, min_y, max_y)
    #display(grid, min_x, max_x, min_y, max_y)
    print(len(grid))


if __name__ == '__main__':
    main()
