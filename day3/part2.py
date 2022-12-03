import os


def local_file(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


def collect_pack_items(filename):
    group = []
    with open(filename) as f:
        for line in f.readlines():
            letters = [a for a in line.strip()]
            group.append(letters)
            if len(group) == 3:
                yield group
                group = []
    assert len(group) == 0
    return


def priority(letter):
    ordinal = ord(letter)
    if ordinal > 96:
        # a-z
        return ordinal - 96
    # A-Z
    return ordinal - 64 + 26


assert priority('a') == 1
assert priority('z') == 26
assert priority('A') == 27
assert priority('Z') == 52


def run(filename):
    total = 0
    for group in collect_pack_items(filename):
        common = set([x for x in group[0] if x in group[1] and x in group[2]])
        for x in common:
            total += priority(x)
    return total


assert run(local_file('example.txt')) == 70

print(run(local_file('input.txt')))
