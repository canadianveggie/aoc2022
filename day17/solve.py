from collections import defaultdict


def local_file(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


def load_moves(filename):
    with open(filename) as f:
        content = f.read():
        return [m for m in content]


def add_voids(voids, centre, distance):
    for y_distance in range(0, distance + 1):
        x_max_distance = distance - y_distance
        x_min = centre[0] - x_max_distance
        x_max = centre[0] + x_max_distance
        voids[centre[1] + y_distance].append((x_min, x_max))
        voids[centre[1] - y_distance].append((x_min, x_max))


def part1(filename, y_examine):
    (sensors, beacons, voids) = load_beacons(filename)
    row_voids = set()
    print(voids[y_examine])
    for (x_min, x_max) in voids[y_examine]:
        for x in range(x_min, x_max + 1):
            coord = (x, y_examine)
            if coord not in sensors and coord not in beacons:
                row_voids.add(coord)
    
    return len(row_voids)


def find_distress_beacon(voids, max_coord):
    for y in range(0, max_coord + 1):
        row_voids = voids[y]
        row_voids.sort()
        covered_range = -1
        for (x_min, x_max) in row_voids:
            if x_min <= covered_range + 1:
                covered_range = max(covered_range, x_max)
            else:
                return (covered_range + 1, y)


def part2(filename, max_coord):
    (sensors, beacons, voids) = load_beacons(filename)
    distress_beacon = find_distress_beacon(voids, max_coord)
    return distress_beacon[0] * 4000000 + distress_beacon[1]


assert part1(local_file('example.txt'), 10) == 26
print(part1(local_file('input.txt'), 2000000))

assert part2(local_file('example.txt'), 20) == 56000011
print(part2(local_file('input.txt'), 4000000))
