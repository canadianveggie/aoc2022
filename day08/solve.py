import os
from collections import defaultdict


def local_file(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


def parse_input(filename):
    trees = list()
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            trees.append([int(x) for x in line])

    return trees


def visible(height, trees_in_direction):
    return len(trees_in_direction) == 0 or height > max(trees_in_direction)


def part1(filename):
    trees = parse_input(filename)
    rows = len(trees)
    columns = len(trees[0])
    total = 0
    for x in range(rows):
        for y in range(columns):
            tree = trees[x][y]
            up = [trees[x][y1] for y1 in range(y+1, rows)]
            down = [trees[x][y1] for y1 in range(0, y)]
            left = [trees[x1][y] for x1 in range(0, x)]
            right = [trees[x1][y] for x1 in range(x+1, columns)]
            if visible(tree, up) or visible(tree, down) or visible(tree, left) or visible(tree, right):
                total += 1
    return total


def scenic(height, trees_in_direction):
    score = 0
    if len(trees_in_direction) == 0:
        return 0
    for i in range(len(trees_in_direction)):
        score += 1
        if height <= trees_in_direction[i]:
            break
    # print(height, trees_in_direction, score)
    return score


def part2(filename):
    trees = parse_input(filename)
    rows = len(trees)
    columns = len(trees[0])
    total = 0
    for x in range(rows):
        for y in range(columns):
            tree = trees[x][y]
            up = [trees[x][y1] for y1 in range(y+1, rows)]
            down = [trees[x][y1] for y1 in range(y-1, -1, -1)]
            left = [trees[x1][y] for x1 in range(x-1, -1, -1)]
            right = [trees[x1][y] for x1 in range(x+1, columns)]
            score = scenic(tree, up) * scenic(tree, down) * scenic(tree, left) * scenic(tree, right)
            # print(x,y,tree,score)
            total = max(total, score)
    return total


assert part1(local_file('example.txt')) == 21
print(part1(local_file('input.txt')))

assert part2(local_file('example.txt')) == 8
print(part2(local_file('input.txt')))
