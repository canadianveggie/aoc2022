import os


def local_file(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


def collect_line_groups(filename, parser=lambda x: x):
    with open(filename) as f:
        group = []
        for line in f.readlines():
            if line.strip() == '':
                yield group
                group = []
            else:
                group.append(parser(line.strip()))
        if len(group) > 0:
            yield group
    return


def part1(filename):
    with open(filename) as f:
        max_total = 0
        
        for elf in collect_line_groups(filename, int):
            elf_total = sum(elf)
            max_total = max(max_total, elf_total)

        return max_total


def part2(filename):
    top3 = []
    for elf in collect_line_groups(filename, int):
        elf_total = sum(elf)
        top3.append(elf_total)
        top3.sort()
        top3 = top3[-3:]

    return sum(top3)


assert part1(local_file('example.txt')) == 24000
print(part1(local_file('input.txt')))

assert part2(local_file('example.txt')) == 45000
print(part2(local_file('input.txt')))
