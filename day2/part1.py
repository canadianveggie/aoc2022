import os


def local_file(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

# A,X = Rock
# B,Y = Paper
# C,Z = Scissors
scores = {
    ('A','X'): 3,
    ('A','Y'): 6,
    ('A','Z'): 0,
    ('B','X'): 0,
    ('B','Y'): 3,
    ('B','Z'): 6,
    ('C','X'): 6,
    ('C','Y'): 0,
    ('C','Z'): 3,
}

bonus = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

def run(filename):
    score = 0
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            them, us = line.split(' ')
            score += scores[(them, us)] + bonus[us]

    print(score)
    return score


assert run(local_file('example.txt')) == 15

print(run(local_file('input.txt')))
