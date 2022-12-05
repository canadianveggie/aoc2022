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
            if line.startswith (' 1'):
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
            elif line.startswith('move'): # moves
                re_match = re.match('move (\\d+) from (\\d+) to (\\d+)', line).groups()
                moves.append([int(x) for x in re_match])

    return crates, moves


def part1(filename):
    crates, moves = parse_input(filename)

    for (count, from_i, to_i) in moves:
        for i in range(count):
            crates[to_i - 1].append(crates[from_i - 1].pop())

    return ''.join([crate[-1] for crate in crates])


def part2(filename):
    crates, moves = parse_input(filename)

    for (count, from_i, to_i) in moves:
        stack = crates[from_i - 1][-1 * count:]
        for i in range(count):
            crates[from_i - 1].pop()
        crates[to_i - 1].extend(stack)

    return ''.join([crate[-1] for crate in crates])


assert part1(local_file('example.txt')) == 'CMZ'
print(part1(local_file('input.txt')))

assert part2(local_file('example.txt')) == 'MCD'
print(part2(local_file('input.txt')))
