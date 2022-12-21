import os


def local_file(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


def load(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def mix(decrypted, encrypted):
    for e in encrypted:
        old_index = decrypted.index(e)
        index_delta = e[1]
        if index_delta != 0:
            decrypted.pop(old_index)
            new_index = old_index + index_delta
            decrypted.insert((old_index + index_delta) % len(decrypted), e)

    return decrypted


def solve(filename, loops=1, decryption_key=1):
    original = load(filename)
    encrypted = [(i, int(original[i]) * decryption_key) for i in range(len(original))]

    decrypted = encrypted.copy()
    for i in range(loops):
        decrypted = mix(decrypted, encrypted)

    zero_element = [x for x in encrypted if x[1] == 0][0]
    zero_index = decrypted.index(zero_element)
    
    specials = [1000, 2000, 3000]
    result = sum([decrypted[(zero_index + x) % len(decrypted)][1] for x in specials])
    return result

def part1(filename):
    return solve(filename)


def part2(filename, loops=10, decryption_key=811589153):
    return solve(filename, loops, decryption_key)


assert part1(local_file('example.txt')) == 3
print(part1(local_file('input.txt')))

assert part2(local_file('example.txt')) == 1623178306
print(part2(local_file('input.txt')))
