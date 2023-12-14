def transpose(grid):
    return list(zip(*grid))

def tilt(line):
    print(line)
    newline = []
    for idx, ch in enumerate(line):
        if ch == 'O':
            back = idx
            moved = False
            while back > 0 and newline[back - 1] == '.':
                moved = True
                back -= 1
            if moved:
                newline[back] = 'O'
                newline.append('.')
            else:
                newline.append(ch)
        else:
            newline.append(ch)
    print(newline)
    return newline

def load(grid):
    total = 0
    line_len = len(grid[0])
    for line in grid:
        for idx, cell in enumerate(line):
            length = line_len - idx
            if cell == 'O':
                total += length
    return total

def main():
    lines = []
    with open('inputs.txt') as f:
        for line in f:
            # convert to chars
            lines.append(list(line.strip()))

    target = []
    transp = transpose(lines)
    for line in transp:
        target.append(tilt(line))
        print()
    print(load(target))

if __name__ == '__main__':
    main()

