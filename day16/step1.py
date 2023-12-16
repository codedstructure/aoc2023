from collections import defaultdict

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

energised = defaultdict(int)

def main():
    global max_row, max_col
    grid = {}
    with open('inputs.txt') as f:
        for row, line in enumerate(f):
            line = line.strip()
            for col, cell in enumerate(line):
                grid[(row, col)] = cell
    max_row = row
    max_col = col
    traverse(grid, (0, 0), RIGHT)

    print(len(energised))

def in_grid(pos):
    r, c = pos
    if r < 0 or c < 0:
        return False
    if r > max_row or c > max_col:
        return False
    return True

def traverse(grid, pos, direction):
    while True:
        if not in_grid(pos):
            break
        if energised[pos] & (1 << direction):
            break
        energised[pos] |= (1 << direction)
        cell = grid[pos]
        if direction in (LEFT, RIGHT):
            if cell in ('-', '.'):
                pos = (pos[0], pos[1] + (1 if direction == RIGHT else -1))
            elif cell == '|':
                traverse(grid, (pos[0] - 1, pos[1]), UP)
                direction = DOWN
                pos = (pos[0] + 1, pos[1])
            elif cell == '\\':
                if direction == RIGHT:
                    direction = DOWN
                    pos = (pos[0] + 1, pos[1])
                else:
                    direction = UP
                    pos = (pos[0] - 1, pos[1])
            elif cell == '/':
                if direction == RIGHT:
                    direction = UP
                    pos = (pos[0] - 1, pos[1])
                else:
                    direction = DOWN
                    pos = (pos[0] + 1, pos[1])
        elif direction in (UP, DOWN):
            if cell in ('|', '.'):
                pos = (pos[0] + (1 if direction == DOWN else -1), pos[1])
            elif cell == '-':
                traverse(grid, (pos[0], pos[1] - 1), LEFT)
                direction = RIGHT
                pos = (pos[0], pos[1] + 1)
            elif cell == '\\':
                if direction == DOWN:
                    direction = RIGHT
                    pos = (pos[0], pos[1] + 1)
                else:
                    direction = LEFT
                    pos = (pos[0], pos[1] - 1)
            elif cell == '/':
                if direction == DOWN:
                    direction = LEFT
                    pos = (pos[0], pos[1] - 1)
                else:
                    direction = RIGHT
                    pos = (pos[0], pos[1] + 1)

if __name__ == '__main__':
    main()
