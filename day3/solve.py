import os


def local_file(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


def priority(letter):
    if letter.islower():
        return ord(letter) - ord('a') + 1
    return ord(letter) - ord('A') + 1 + 26


assert priority('a') == 1
assert priority('z') == 26
assert priority('A') == 27
assert priority('Z') == 52


def collect_pack_compartments(filename):
    with open(filename) as f:
        for line in f.readlines():
            letters = [a for a in line.strip()]
            mid = len(letters) // 2
            yield (letters[:mid], letters[mid:])
    return


def part1(filename):
    total = 0
    for compartment1, compartment2 in collect_pack_compartments(filename):
        common = set(compartment1) & set(compartment2)
        for x in common:
            total += priority(x)
    return total


def collect_groups(filename):
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


def part2(filename):
    total = 0
    for group in collect_groups(filename):
        common = set(group[0]) & set(group[1]) & set(group[2])
        for x in common:
            total += priority(x)
    return total


assert part1(local_file('example.txt')) == 157
print(part1(local_file('input.txt')))

assert part2(local_file('example.txt')) == 70
print(part2(local_file('input.txt')))
