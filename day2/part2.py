import os


def local_file(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


# A,X = Rock
# B,Y = Paper
# C,Z = Scissors
# X = Lose
# Y = Draw
# Z = Win
scores = {
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


def run(filename):
    score = 0
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            them, us = line.split(' ')
            score += scores[(them, us)]

    print(score)
    return score


assert run(local_file('example.txt')) == 12

print(run(local_file('input.txt')))
