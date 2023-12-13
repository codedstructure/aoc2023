
def check_numbers(line, prevline, nextline):
    line = "." + line + "."
    prevline = "." + prevline + "."
    nextline = "." + nextline + "."
    parts = []
    number = None
    validpart = False
    for idx, ch in enumerate(line[1:-1]):
        if ch.isdigit():
            if number is None:
                number = int(ch)
            else:
                number = number * 10 + int(ch)
            if nextline[idx+2] not in "0123456789.":
                validpart = True
            if nextline[idx+1] not in "0123456789.":
                validpart = True
            if nextline[idx] not in "0123456789.":
                validpart = True
            if prevline[idx+2] not in "0123456789.":
                validpart = True
            if prevline[idx+1] not in "0123456789.":
                validpart = True
            if prevline[idx] not in "0123456789.":
                validpart = True
        elif ch != ".":
            validpart = True
            if number is not None:
                parts.append(number)
                number = None
        else:
            if validpart and number is not None:
                parts.append(number)
            validpart = False
            number = None
    if validpart and number is not None:
        parts.append(number)

    return parts

def main():
    with open('inputs.txt') as f:
        lines = f.readlines()

    lines = list(map(str.strip, lines))

    total = 0
    for idx, line in enumerate(lines):
        prevline = lines[idx-1] if idx > 0 else "." * len(line)
        nextline = lines[idx+1] if idx < len(lines)-1 else "." * len(line)
        parts = check_numbers(line, prevline, nextline)
        total += sum(parts)
    print(total)


if __name__ == '__main__':
    main()
