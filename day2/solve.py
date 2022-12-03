import os


def local_file(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


# A,X = Rock
# B,Y = Paper
# C,Z = Scissors
# X = Lose
# Y = Draw
# Z = Win
scores_part1 = {
    ('A', 'X'): 3,
    ('A', 'Y'): 6,
    ('A', 'Z'): 0,
    ('B', 'X'): 0,
    ('B', 'Y'): 3,
    ('B', 'Z'): 6,
    ('C', 'X'): 6,
    ('C', 'Y'): 0,
    ('C', 'Z'): 3,
}

bonus_part1 = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

scores_part2 = {
    ('A', 'X'): 0+3,
    ('A', 'Y'): 3+1,
    ('A', 'Z'): 6+2,
    ('B', 'X'): 0+1,
    ('B', 'Y'): 3+2,
    ('B', 'Z'): 6+3,
    ('C', 'X'): 0+2,
    ('C', 'Y'): 3+3,
    ('C', 'Z'): 6+1,
}


def part1(filename):
    score = 0
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            them, us = line.split(' ')
            score += scores_part1[(them, us)] + bonus_part1[us]

    return score


def part2(filename):
    score = 0
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            them, us = line.split(' ')
            score += scores_part2[(them, us)]

    return score


assert part1(local_file('example.txt')) == 15
print(part1(local_file('input.txt')))

assert part2(local_file('example.txt')) == 12
print(part2(local_file('input.txt')))
