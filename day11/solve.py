import functools
import operator


class Monkey(object):
    def __init__(self, starting_items, operation, test_divisor, next_monkeys):
        self.items = starting_items
        self.operation = operation
        self.test_divisor = test_divisor
        self.next_monkeys = next_monkeys
        self.inspected = 0

    def inspect(self, stress_divisor=1, stress_modulo=1):
        while len(self.items) > 0:
            item = self.items.pop(0)
            item = self.operation(item)
            item = (item // stress_divisor) % stress_modulo
            result = item % self.test_divisor == 0
            self.inspected += 1
            yield (item, self.next_monkeys[result])


def print_monkeys(monkeys):
    for i in range(len(monkeys)):
        monkey = monkeys[i]
        print(f'Monkey {i}({monkey.inspected}): {monkey.items}')


def simulate(monkeys, rounds=20, stress_divisor=1, stress_modulo=1):
    #print_monkeys(monkeys)
    for i in range(rounds):
        for monkey in monkeys:
            for (item, next_monkey) in monkey.inspect(stress_divisor, stress_modulo):
                monkeys[next_monkey].items.append(item)
        if (i+1) % 100 == 0:
            print(f'Round {i+1}')
            print_monkeys(monkeys)

    inspections = [m.inspected for m in monkeys]
    inspections.sort()
    return inspections[-1] * inspections[-2]


def part1(monkeys):
    stress_modulo = functools.reduce(operator.mul, [m.test_divisor for m in monkeys])
    return simulate(monkeys, rounds=20, stress_divisor=3, stress_modulo=stress_modulo)


def part2(monkeys):
    stress_modulo = functools.reduce(operator.mul, [m.test_divisor for m in monkeys])
    return simulate(monkeys, rounds=10000, stress_divisor=1, stress_modulo=stress_modulo)


example_monkeys = [
    Monkey(
        [79, 98],
        lambda old: old * 19,
        23,
        {True: 2, False: 3}
    ),
    Monkey(
        [54, 65, 75, 74],
        lambda old: old + 6,
        19,
        {True: 2, False: 0}
    ),
    Monkey(
        [79, 60, 97],
        lambda old: old * old,
        13,
        {True: 1, False: 3}
    ),
    Monkey(
        [74],
        lambda old: old + 3,
        17,
        {True: 0, False: 1}
    ),
]


input_monkeys = [
    Monkey(
      [65, 58, 93, 57, 66],
      lambda old: old * 7,
      19,
      { True: 6, False: 4 },
    ),
    Monkey(
      [76, 97, 58, 72, 57, 92, 82],
      lambda old: old + 4,
      3,
      { True: 7, False: 5 },
    ),
    Monkey(
      [90, 89, 96],
      lambda old: old * 5,
      13,
      { True: 5, False: 1 },
    ),
    Monkey(
      [72, 63, 72, 99],
      lambda old: old * old,
      17,
      { True: 0, False: 4 },
    ),
    Monkey(
      [65],
      lambda old: old + 1,
      2,
      { True: 6, False: 2 },
    ),
    Monkey(
      [97, 71],
      lambda old: old + 8,
      11,
      { True: 7, False: 3 },
    ),
    Monkey(
      [83, 68, 88, 55, 87, 67],
      lambda old: old + 2,
      5,
      { True: 2, False: 1 },
    ),
    Monkey(
      [64, 81, 50, 96, 82, 53, 62, 92],
      lambda old: old + 5,
      7,
      { True: 3, False: 0 },
    ),
]


# assert part1(example_monkeys) == 10605
# print(part1(input_monkeys))

assert part2(example_monkeys) == 2713310158
print(part2(input_monkeys))
