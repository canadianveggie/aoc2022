import os


def local_file(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


def parse_input(filename):
    x = 1
    signals = []
    with open(filename) as f:
        for line in f.readlines():
            signals.append(x)
            line = line.strip()
            if line == 'noop':
                # do nothing
                pass
            elif line.startswith('addx '):
                signals.append(x)
                delta_x = int(line.split(' ')[1])
                x += delta_x
            else:
                print(f'Unknown command {line}')
    return (x, signals)


assert(parse_input(local_file('example_small.txt'))) == (-1, [1, 1, 1, 4, 4])

def part1(filename):
    x, signals = parse_input(filename)
    s = sum([i * signals[i-1] for i in [20, 60, 100, 140, 180, 220]])
    return s


def draw(signals, width=40):
    lines = []
    for i in range(len(signals)):
        col = i % width

        if col == 0:
            lines.append('')

        if col - 1 <= signals[i] <= col + 1:
            lines[-1] += '#'
        else:
            lines[-1] += '.'

    return lines

def part2(filename):
    x, signals = parse_input(filename)
    return draw(signals)

assert part1(local_file('example.txt')) == 13140
print(part1(local_file('input.txt')))


expected = [
    '##..##..##..##..##..##..##..##..##..##..',
    '###...###...###...###...###...###...###.',
    '####....####....####....####....####....',
    '#####.....#####.....#####.....#####.....',
    '######......######......######......####',
    '#######.......#######.......#######.....'
]
assert part2(local_file('example.txt')) == expected
print('\n'.join(part2(local_file('input.txt'))))


