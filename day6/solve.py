import os
import re


def local_file(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


def parse_input(filename):
    with open(filename) as f:
        crate_def = True
        crates = []
        moves = []
        for line in f.readlines():
            if line.startswith(' 1'):
                crate_def = False
            elif crate_def:
                letters = [x for x in line]
                i = 0
                for box in zip(*[iter(letters)]*4):
                    if len(crates) <= i:
                        crates.append(list())
                    if box[1] != ' ':
                        crates[i].insert(0, box[1])
                    i += 1
            elif line.startswith('move'):  # moves
                re_match = re.match('move (\\d+) from (\\d+) to (\\d+)', line).groups()
                moves.append([int(x) for x in re_match])

    return crates, moves


def part1(filename):
    with open(filename) as f:
        data = f.read()
        i = 0
        size = 4
        while i < len(data) - size:
            print(set(data[i: i + size]))
            if len(set(data[i: i + size])) == size:
                return i + size
            i += 1


def part2(filename):
    with open(filename) as f:
        data = f.read()
        i = 0
        size = 14
        while i < len(data) - size:
            print(set(data[i: i + size]))
            if len(set(data[i: i + size])) == size:
                return i + size
            i += 1


assert part1(local_file('example.txt')) == 5
print(part1(local_file('input.txt')))

# assert part2(local_file('example.txt')) == 19
print(part2(local_file('input.txt')))
