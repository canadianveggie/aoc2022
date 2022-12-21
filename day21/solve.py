import os
import re


def local_file(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


class Monkey(object):
    def __init__(self, name, value=None, monkey1=None, monkey2=None, operator=None):
        self.name = name
        self.value = value
        self.monkey1 = monkey1
        self.monkey2 = monkey2
        self.operator = operator

    def return_value(self, monkeys):
        if self.value is not None:
            return int(self.value)
        else:
            m1 = monkeys[self.monkey1].return_value(monkeys)
            m2 = monkeys[self.monkey2].return_value(monkeys)
            if self.operator == '+':
                return m1 + m2
            elif self.operator == '-':
                return m1 - m2
            elif self.operator == '*':
                return m1 * m2
            elif self.operator == '/':
                return m1 / m2
            elif self.operator == '==':
                return (m1 == m2, m1, m2)
            else:
                raise Exception(f'Unknown operator {self.operator}')


def load(filename):
    monkeys = dict()
    with open(filename) as f:
        for line in f.readlines():
            m = re.match(r"(\w{4}): ((\d+)|((\w{4}) (.+) (\w{4})))", line)
            name = m.groups()[0]
            # print(name, m.groups()[2], m.groups()[4], m.groups()[6], m.groups()[5])
            monkeys[name] = Monkey(name, m.groups()[2], m.groups()[4], m.groups()[6], m.groups()[5])
    return monkeys


def part1(filename):
    monkeys = load(filename)
    return monkeys['root'].return_value(monkeys)


def part2(filename):
    monkeys = load(filename)
    monkeys['root'].operator = '=='
    small_i = 1
    big_i = 1000000000000000
    while True:
        i = int(small_i + (big_i - small_i) / 2)
        monkeys['humn'].value = i
        result = monkeys['root'].return_value(monkeys)
        # print(i, result)
        if result[0]:
            return i
        elif result[1] - result[2] > 0:
            small_i = i
        else:
            big_i = i
    return i


assert part1(local_file('example.txt')) == 152
print(part1(local_file('input.txt')))

# assert part2(local_file('example.txt')) == 301
print(part2(local_file('input.txt')))
