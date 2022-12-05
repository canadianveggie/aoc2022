import os


def local_file(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


def collect_assignments(filename):
    with open(filename) as f:
        for line in f.readlines():
            a1, a2 = line.strip().split(',')
            yield ([int(x) for x in a1.split('-')], [int(x) for x in a2.split('-')])
    return


def contained(elf1, elf2):
    return elf1[0] >= elf2[0] and elf1[1] <= elf2[1]


def part1(filename):
    total = 0
    for elf1, elf2 in collect_assignments(filename):
        if contained(elf1, elf2) or contained(elf2, elf1):
            total += 1
    return total


def overlap(elf1, elf2):
    return elf2[0] <= elf1[0] <= elf2[1] or elf2[0] <= elf1[1] <= elf2[1]


def part2(filename):
    total = 0
    for elf1, elf2 in collect_assignments(filename):
        if overlap(elf1, elf2) or overlap(elf2, elf1):
            total += 1
    return total


assert part1(local_file('example.txt')) == 2
print(part1(local_file('input.txt')))

assert part2(local_file('example.txt')) == 4
print(part2(local_file('input.txt')))
