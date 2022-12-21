import os


def local_file(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


def load_droplets(filename):
    droplets = set()
    with open(filename) as f:
        for line in f.readlines():
            droplets.add(tuple([int(x) for x in line.split(',')]))
    return droplets


def adjacent_coords(coord):
    return [
        (coord[0]-1, coord[1], coord[2]),
        (coord[0]+1, coord[1], coord[2]),
        (coord[0], coord[1]-1, coord[2]),
        (coord[0], coord[1]+1, coord[2]),
        (coord[0], coord[1], coord[2]-1),
        (coord[0], coord[1], coord[2]+1),
    ]

def part1(filename):
    droplets = load_droplets(filename)

    surface_area = 0
    for droplet in droplets:
        for adj in adjacent_coords(droplet):
            if adj not in droplets:
                surface_area += 1

    return surface_area


def find_outside_air(droplets):
    min_coord = tuple([min([x[0] for x in droplets]), min([x[1] for x in droplets]), min([x[2] for x in droplets])])
    max_coord = tuple([max([x[0] for x in droplets]), max([x[1] for x in droplets]), max([x[2] for x in droplets])])
    outside_air = set()
    for x in [min_coord[0]-1, max_coord[0]+1]:
        for y in range(min_coord[1]-1, max_coord[1] + 2):
            for z in range(min_coord[2]-1, max_coord[2] + 2):
                outside_air.add(tuple([x,y,z]))
    for y in [min_coord[1]-1, max_coord[1]+1]:
        for x in range(min_coord[0]-1, max_coord[0] + 2):
            for z in range(min_coord[2]-1, max_coord[2] + 2):
                outside_air.add(tuple([x,y,z]))
    for z in [min_coord[2]-1, max_coord[2]+1]:
        for x in range(min_coord[0]-1, max_coord[0] + 2):
            for y in range(min_coord[1]-1, max_coord[1] + 2):
                outside_air.add(tuple([x,y,z]))


    changes = True
    while changes:
        changes = False
        for x in range(min_coord[0], max_coord[0] + 1):
            for y in range(min_coord[1], max_coord[1] + 1):
                for z in range(min_coord[2], max_coord[2] + 1):
                    coord = (x,y,z)
                    if coord not in droplets and coord not in outside_air:
                        if any([adj in outside_air for adj in adjacent_coords(coord)]):
                            outside_air.add(coord)
                            changes = True

    return outside_air


def part2(filename):
    droplets = load_droplets(filename)
    outside_air = find_outside_air(droplets)

    surface_area = 0
    for droplet in droplets:
        for adj in adjacent_coords(droplet):
            if adj in outside_air:
                surface_area += 1

    return surface_area


assert part1(local_file('example.txt')) == 64
print(part1(local_file('input.txt')))

assert part2(local_file('example.txt')) == 58
print(part2(local_file('input.txt')))
