
def matches(pattern, groups):
    in_group = False
    groups = groups[:]
    groups.reverse()
    group_count = 0
    try:
        for ch in pattern:
            if in_group:
                if ch == '.':
                    if group_count != groups.pop():
                        return False
                    in_group = False
                    group_count = 0
                else:
                    group_count += 1
            elif ch == '#':
                if not groups:
                    return False
                group_count = 1
                in_group = True

        return not groups or (len(groups) == 1 and group_count == groups.pop())
    except IndexError:
        return False

def possibles(line):
    pattern, constraint = line.split()
    count = line.count('?')
    groups = list(map(int, constraint.split(',')))

    result = 0
    for i in range(1 << count):
        new_line = []
        x = i
        for ch in pattern:
            if ch == '?':
                new_line.append('#' if x % 2 == 1 else '.')
                x //= 2
            else:
                new_line.append(ch)
        new_pattern = ''.join(new_line)

        if matches(new_pattern, groups):
            result += 1
    return result

def main():
    total = 0
    with open('inputs.txt') as f:
        for line in f:
            total += possibles(line.strip())
    print(total)


if __name__ == '__main__':
    main()
