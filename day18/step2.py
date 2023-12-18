# Here pos is x, y (rather than row, col)

# https://en.wikipedia.org/wiki/Shoelace_formula
def shoelace(instructions):
    boundary_len = 0
    x, y = 0, 0
    points = []

    # Define direction vectors
    dir_dxy = {'U': (0, -1), 'R': (1, 0), 'D': (0, 1), 'L': (-1, 0)}

    # Calculate points (assumes no self-intersection)
    for dir, length in instructions:
        boundary_len += length
        dx, dy = dir_dxy[dir]
        x, y = x + dx * length, y + dy * length
        points.append((x, y))

    # Gauss' Shoelace formula
    area = 0.5 * abs(
        sum(x*y_next - y*x_next for ((x, y), (x_next, y_next))
            in zip(points, points[1:] + points[:1]))
    )

    # Testing on simple areas (e.g. R3,D3,L3,U3) shows that ~half the boundary
    # is already included in the calculated area (e.g. 'internal' area is
    # 9 for this 4x4 square with boundary length 12).
    return int(area + boundary_len / 2 + 1)

def col_to_dirdist(col):
    # example col: '(#123456)'
    val = int(col[2:-1], 16)
    dist, dir = divmod(val, 16)
    return {0: 'R', 1: 'D', 2: 'L', 3: 'U'}[dir], dist

def main():
    instrs = []
    with open('inputs.txt') as f:
        for line in f:
            dir, length, col = line.split()
            instrs.append(col_to_dirdist(col))

    print(shoelace(instrs))


if __name__ == '__main__':
    main()
