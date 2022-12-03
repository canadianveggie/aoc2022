import os


def local_file(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


def collect_pack_items(filename):
    with open(filename) as f:
        for line in f.readlines():
            letters = [a for a in line.strip()]
            mid = len(letters) // 2
            yield (letters[:mid], letters[mid:])
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
    for compartment1, compartment2 in collect_pack_items(filename):
        common = set([x for x in compartment1 if x in compartment2])
        for x in common:
            total += priority(x)
    return total


assert run(local_file('example.txt')) == 157

print(run(local_file('input.txt')))
