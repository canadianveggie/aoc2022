import os


def local_file(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


def load_rocks(filename):
    rocks = dict()
    with open(filename) as f:
        for line in f.readlines():
            prev = None
            for coord in line.split('->'):
                (x_str, y_str) = coord.strip().split(',')
                x = int(x_str)
                y = int(y_str)
                if prev is not None:
                    for x1 in range(min(x, prev[0]), max(x, prev[0]) + 1):
                        for y1 in range(min(y, prev[1]), max(y, prev[1]) + 1):
                            rocks[(x1, y1)] = True
                prev = (x, y)
    return rocks


def add_sand(coords, pos, bottom):
    if pos[1] > bottom:
        return False

    possible_next_pos = [(pos[0], pos[1] + 1), (pos[0] - 1, pos[1] + 1), (pos[0] + 1, pos[1] + 1)]
    for next_pos in possible_next_pos:
        if next_pos not in coords:
            return add_sand(coords, next_pos, bottom)

    if pos not in coords:
        coords[pos] = True
        return True

    raise Exception('where is this sand going???')


def part1(filename):
    coords = load_rocks(filename)
    grains_of_sand = 0

    bottom = max(c[1] for c in coords.keys())
    while add_sand(coords, (500, 0), bottom):
        grains_of_sand += 1
    return grains_of_sand


def add_sand_inifinite_bottom(coords, pos, infinite_bottom):
    possible_next_pos = [(pos[0], pos[1] + 1), (pos[0] - 1, pos[1] + 1), (pos[0] + 1, pos[1] + 1)]
    for next_pos in possible_next_pos:
        if next_pos not in coords and pos[1] < infinite_bottom:
            return add_sand_inifinite_bottom(coords, next_pos, infinite_bottom)

    if pos not in coords:
        coords[pos] = True
        return True

    raise Exception('where is this sand going???')


def part2(filename):
    coords = load_rocks(filename)
    grains_of_sand = 0

    bottom = max(c[1] for c in coords.keys()) + 1
    source = (500, 0)
    while add_sand_inifinite_bottom(coords, source, bottom):
        grains_of_sand += 1
        if source in coords:
            break
    return grains_of_sand


assert part1(local_file('example.txt')) == 24
print(part1(local_file('input.txt')))

assert part2(local_file('example.txt')) == 93
print(part2(local_file('input.txt')))
