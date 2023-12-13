from collections import defaultdict

gear_idx = defaultdict(list)


def update_gears(linenum, line, prevline, nextline):
    line = "." + line + "."
    prevline = "." + prevline + "."
    nextline = "." + nextline + "."
    number = None
    maybegear = False
    gearidx = set()
    for idx, ch in enumerate(line[1:-1]):
        if ch.isdigit():
            if number is None:
                number = int(ch)
            else:
                number = number * 10 + int(ch)
            if nextline[idx+2] == '*':
                gearidx.add((linenum+1, idx+1))
                maybegear = True
            if nextline[idx+1] == '*':
                gearidx.add((linenum+1, idx))
                maybegear = True
            if nextline[idx] == '*':
                gearidx.add((linenum+1, idx-1))
                maybegear = True
            if prevline[idx+2] == '*':
                gearidx.add((linenum-1, idx+1))
                maybegear = True
            if prevline[idx+1] == '*':
                gearidx.add((linenum-1, idx))
                maybegear = True
            if prevline[idx] == '*':
                gearidx.add((linenum-1, idx-1))
                maybegear = True
        elif ch == "*":
            maybegear = True
            gearidx.add((linenum, idx))
            if number is not None:
                for loc in gearidx:
                    gear_idx[loc].append(number)
                number = None
        else:
            if maybegear and number is not None:
                for loc in gearidx:
                    gear_idx[loc].append(number)
            gearidx.clear()
            maybegear = False
            number = None
    if maybegear and number is not None:
        for loc in gearidx:
            gear_idx[loc].append(number)
        gearidx.clear()

def main():

    with open('inputs.txt') as f:
        lines = f.readlines()

    lines = list(map(str.strip, lines))

    total = 0

    for idx, line in enumerate(lines):
        prevline = lines[idx-1] if idx > 0 else "." * len(line)
        nextline = lines[idx+1] if idx < len(lines)-1 else "." * len(line)
        update_gears(idx, line, prevline, nextline)

    for gear in gear_idx.values():
        if len(gear) == 2:
            total += gear[0] * gear[1]
    print(total)


if __name__ == '__main__':
    main()
