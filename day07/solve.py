import os
from collections import defaultdict


def local_file(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


def parse_input(filename):
    dir_sizes = defaultdict(int)
    with open(filename) as f:
        current_dir = list()
        for line in f.readlines():
            line = line.strip()
            if line == '$ cd /':
                current_dir.append('/')
            elif line == '$ cd ..':
                # pop dir
                current_dir.pop()
            elif line.startswith('$ cd '):
                directory = '/'.join(current_dir) + line.replace('$ cd ', '')
                current_dir.append(directory)
            elif line.startswith('dir') or line.startswith('$'):
                pass
            else:
                size = int(line.split(' ')[0])
                for d in current_dir:
                    dir_sizes[d] += size

    # print(dir_sizes)
    return dir_sizes


def part1(filename):
    sizes = parse_input(filename)
    return sum([s for s in sizes.values() if s <= 100000])


def part2(filename):
    sizes = parse_input(filename)
    free = 70000000 - sizes['/']
    target = 30000000 - free
    targets = [s for s in sizes.values() if s >= target]
    targets.sort()
    return targets[0]


assert part1(local_file('example.txt')) == 95437
print(part1(local_file('input.txt')))

assert part2(local_file('example.txt')) == 24933642
print(part2(local_file('input.txt')))
