
def pairwise_diff(seq):
    result = []
    seq = list(seq)
    for idx in range(len(seq) - 1):
        result.append(seq[idx + 1] - seq[idx])
    return result

def seq_next(seq):
    next_diffs = list(seq)
    accum = []
    while len(set(next_diffs)) != 1:
        accum.append(next_diffs.copy())
        next_diffs = pairwise_diff(next_diffs)

    inc = next_diffs[0]
    while accum:
        acc = accum.pop()
        acc.insert(0, acc[0] - inc)
        inc = acc[0]
    return acc[0]

def main():
    total = 0
    with open('inputs.txt') as f:
        for line in f:
            total += seq_next(map(int, line.split()))

    print(total)

if __name__ == '__main__':
    main()
