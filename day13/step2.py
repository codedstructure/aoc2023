
def transpose(lines):
    return list(zip(*lines))

def diff_count(s1, s2):
    diff = 0
    for a, b in zip(s1, s2):
        if a != b:
            diff += 1
    return diff

def compare_smudged(left, right):

    smudges = 0
    for (l, r) in zip(left, right):
        smudges += diff_count(l, r)
    return smudges == 1

def find_y_mirror(lines):
    # return number of lines before a reflection, or 0 if no reflection.
    for idx in range(1, len(lines) // 2 + 1):
        left = lines[:idx]
        right = lines[idx:idx*2]
        assert len(left) == len(right)
        right.reverse()
        if compare_smudged(left, right):
            return idx
        left = lines[-idx*2:-idx]
        right = lines[-idx:]
        right.reverse()
        assert len(left) == len(right)
        if compare_smudged(left, right):
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
