import os


def local_file(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


def find_signal(text, size):
    i = size
    while i < len(text):
        if len(set(text[i - size: i])) == size:
            return i
        i += 1


def part1(text):
    return find_signal(text, 4)


def part2(text):
    return find_signal(text, 14)


assert part1('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
assert part1('nppdvjthqldpwncqszvftbrmjlhg') == 6
assert part1('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
assert part1('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11
print(part1(open(local_file('input.txt')).read()))

assert part2('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 19
assert part2('bvwbjplbgvbhsrlpgdmjqwftvncz') == 23
assert part2('nppdvjthqldpwncqszvftbrmjlhg') == 23
assert part2('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 29
assert part2('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 26
print(part2(open(local_file('input.txt')).read()))
