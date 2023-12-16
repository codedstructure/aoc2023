
def ihash(inst):
    h = 0
    for ch in inst:
        h = ((h + ord(ch)) * 17) % 256
    print(inst, h)
    return h


def main():
    with open('inputs.txt') as f:
        instructions = f.read().strip().split(',')

    print(sum(ihash(inst) for inst in instructions))


if __name__ == '__main__':
    main()
