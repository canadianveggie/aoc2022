import os


def local_file(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


def parse_input(filename):
    with open(filename) as f:
        for line in f.readlines():
            (direction, spaces) = line.strip().split(' ')
            yield (direction, int(spaces))

def adjust_head(head, direction):
    if direction == 'U':
        return (head[0], head[1] + 1)
    elif direction == 'D':
        return (head[0], head[1] - 1)
    elif direction == 'R':
        return (head[0] + 1, head[1])
    elif direction == 'L':
        return (head[0] - 1, head[1])
    else:
        print(f'Unknown direction {direction}')

def adjust_tail(head, tail):
    delta_x = head[0] - tail[0]
    delta_y = head[1] - tail[1]

    # head has to be at least 2 spaces away in 1 dimension to provide space for tail to move
    if abs(delta_x) >= 2 or abs(delta_y) >= 2:
        # move up to 1 space in each direction if that gets us closer
        # lack of sign function in python is annoying here
        if delta_x <= -1:
            tail = (tail[0] - 1, tail[1])
        elif delta_x >= 1:
            tail = (tail[0] + 1, tail[1])
        
        if delta_y <= -1:
            tail = (tail[0], tail[1] - 1)
        elif delta_y >= 1:
            tail = (tail[0], tail[1] + 1)

    return tail

def part1(filename):
    moves = parse_input(filename)
    visited = set()

    head = (0, 0)
    tail = (0, 0)

    visited.add(tail)

    for direction, spaces in moves:
        for i in range(spaces):
            head = adjust_head(head, direction)
            tail = adjust_tail(head, tail)
            visited.add(tail)

    return len(visited)


def part2(filename):
    moves = parse_input(filename)
    visited = set()

    knots = [(0, 0)] * 10

    visited.add(knots[-1])

    for direction, spaces in moves:
        for i in range(spaces):
            knots[0] = adjust_head(knots[0], direction)
            for i in range(1, len(knots)):
                knots[i] = adjust_tail(knots[i-1], knots[i])
            visited.add(knots[-1])

    return len(visited)


assert part1(local_file('example.txt')) == 13
print(part1(local_file('input.txt')))

assert part2(local_file('example.txt')) == 1
assert part2(local_file('example2.txt')) == 36
print(part2(local_file('input.txt')))
