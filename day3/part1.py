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
    if letter.islower():
        return ord(letter) - ord('a') + 1
    return ord(letter) - ord('A') + 1 + 26


assert priority('a') == 1
assert priority('z') == 26
assert priority('A') == 27
assert priority('Z') == 52


def run(filename):
    total = 0
    for compartment1, compartment2 in collect_pack_items(filename):
        common = set(compartment1) & set(compartment2)
        for x in common:
            total += priority(x)
    return total


assert run(local_file('example.txt')) == 157

print(run(local_file('input.txt')))
