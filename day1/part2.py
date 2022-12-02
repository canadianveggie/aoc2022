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


def run(filename):
    top3 = []
    for elf in collect_line_groups(filename, int):
        elf_total = sum(elf)
        top3.append(elf_total)
        top3.sort()
        top3 = top3[-3:]

    return sum(top3)


assert run(local_file('example.txt')) == 45000

print(run(local_file('input.txt')))
