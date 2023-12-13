
def get_races():
    with open('inputs2.txt') as f:
        lines = f.readlines()
    times = map(int, lines[0].split()[1:])
    dists = map(int, lines[1].split()[1:])

    return list(zip(times, dists))


def winning_dists(race):
    win_dists = []
    time, dist = race
    for hold_time in range(time):
        if (time - hold_time) * hold_time > dist:
            win_dists.append(hold_time)
    return win_dists


def main():
    races = get_races()
    product = 1
    for race in races:
        product *= len(winning_dists(race))
    print(product)


if __name__ == '__main__':
    main()
