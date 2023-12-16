def transpose(grid):
    return list(zip(*grid))

def rotate(grid):
    return list(zip(*reversed(grid)))

def printgrid(grid):
    for row in grid:
        print(''.join(row))
    print()

def tilt(line):
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
    return newline

def spincycle(grid):
    # rotate 90deg three times so 'North' is <- direction
    grid = rotate(rotate(rotate(grid)))
    for _ in range(4):
        target = []
        for line in grid:
            target.append(tilt(line))
        grid = rotate(target)
    grid = rotate(grid)  # undo initial rotate-left
    return grid

def load(grid):
    # Orient North <-
    grid = rotate(rotate(rotate(grid)))
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

    load_samples = []
    grid = lines
    for _ in range(300):
        grid = spincycle(grid)
        #printgrid(grid)
        load_samples.append(load(grid))

    # Ideally would use https://en.wikipedia.org/wiki/Cycle_detection to
    # determine the cycle.

    #head_length = 2  # by inspection (test data)
    #cycle_length = 7  # by inspection (test data)
    head_length = 141
    cycle_length = 28

    #print(load_samples[:head_length])
    #print(load_samples[head_length:head_length+5])
    #print()
    #for i in range(9):
    #    print(load_samples[head_length + cycle_length * i: head_length+cycle_length * (i+1)])

    full_cycles = 1_000_000_000

    offset = ((full_cycles - head_length) % cycle_length)
    print(offset)
    # -1 because samples are 1-based, i.e. first entry is after 1 spin cycle.
    print(load_samples[head_length + offset - 1])

    # 99441 is too low
    # not 99867

if __name__ == '__main__':
    main()

