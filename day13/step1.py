
def transpose(lines):
    return list(zip(*lines))

def find_y_mirror(lines):
    # return number of lines before a reflection, or 0 if no reflection.
    for idx in range(1, len(lines) // 2 + 1):
        left = lines[:idx]
        right = lines[idx:idx*2]
        assert len(left) == len(right)
        right.reverse()
        if left == right:
            return idx
        left = lines[-idx*2:-idx]
        right = lines[-idx:]
        right.reverse()
        assert len(left) == len(right)
        if left == right:
            return len(lines) - idx

    return 0

def process(shape):
    t = 100 * find_y_mirror(shape)
    shape = transpose(shape)
    t += find_y_mirror(shape)
    return t

def main():
    with open('inputs.txt') as f:

        shapes = []
        lines = []
        for line in f:
            line = line.strip()
            if not line:
                shapes.append(lines[:])
                lines = []
            else:
                lines.append(line)
        if lines:
            shapes.append(lines)

    total = 0
    for shape in shapes:
        total += process(shape)
    print(total)


if __name__ == '__main__':
    main()
