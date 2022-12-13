import json
import os
from functools import cmp_to_key


def local_file(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


def parse_input(filename):
    with open(filename) as f:
        while True:
            left = f.readline()
            right = f.readline()
            blank = f.readline()

            if left and right:
                yield (json.loads(left), json.loads(right))
            else:
                break


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right
    else:
        left_list = left if isinstance(left, list) else [left]
        right_list = right if isinstance(right, list) else [right]
        for i in range(max(len(left_list), len(right_list))):
            if i >= len(left_list):
                return -1
            if i >= len(right_list):
                return 1
            c = compare(left_list[i], right_list[i])
            if c != 0:
                return c
            # else - go to next element in the list

    return 0


def part1(filename):
    score = 0
    i = 1
    for (left, right) in parse_input(filename):
        comparison = compare(left, right)
        if comparison <= 0:
            score += i
        i += 1
    return score


def part2(filename):
    signal1 = [[2]]
    signal2 = [[6]]
    all_items = [signal1, signal2]
    for (left, right) in parse_input(filename):
        all_items.append(left)
        all_items.append(right)

    all_items = sorted(all_items, key=cmp_to_key(compare))
    return (all_items.index(signal1) + 1) * (all_items.index(signal2) + 1)


assert part1(local_file('example.txt')) == 13
print(part1(local_file('input.txt')))

assert part2(local_file('example.txt')) == 140
print(part2(local_file('input.txt')))
