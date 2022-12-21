import os
import re


def local_file(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


minerals = ['ore', 'clay', 'obsidian', 'geode']

class BluePrint(object):
    def __init__(self, id, robot_costs: dict):
        self.id = id
        self.robot_costs = robot_costs


class State(object):
    def __init__(self):
        self.materials = dict()
        self.robots = dict()
        for mineral in minerals:
            self.materials[mineral] = 0
            self.robots[mineral] = 0

    def find_choices(self, blueprint: BluePrint):
        choices = [None]
        for mineral in minerals:
            cost = blueprint.robot_costs[mineral]
            buildable = all([self.materials[ingredient] >= cost[ingredient] for ingredient in cost.keys()])
            if buildable:
                choices.append(mineral)
        choices.reverse()
        return choices[:2]

    def increment_time(self):
        for mineral in self.robots.keys():
            self.materials[mineral] += self.robots[mineral]

    def subtract_cost(self, cost):
        for ingredient in cost.keys():
            self.materials[ingredient] -= cost[ingredient]

    def add_robot(self, mineral):
        self.robots[mineral] += 1

    def copy(self):
        c = State()
        c.materials = dict(self.materials)
        c.robots = dict(self.robots)
        return c


def most_geodes(blueprint: BluePrint, state: State, time_left=24):
    if time_left <= 0:
        return state.materials['geode']

    choices = state.find_choices(blueprint)
    max_result = 0
    for c in choices:
        next_state = state.copy()
        if c is not None:
            next_state.subtract_cost(blueprint.robot_costs[c])
        next_state.increment_time()
        if c is not None:
            next_state.add_robot(c)
        max_result = max(max_result, most_geodes(blueprint, next_state, time_left - 1))

    return max_result



def load(filename):
    blueprints = list()
    with open(filename) as f:
        for line in f.readlines():
            m = re.match(r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.", line)
            id = int(m.groups()[0])
            costs = {
                'ore': {
                    'ore': int(m.groups()[1]),
                },
                'clay': {
                    'ore': int(m.groups()[2]),
                },
                'obsidian': {
                    'ore': int(m.groups()[3]),
                    'clay': int(m.groups()[4]),
                },
                'geode': {
                    'ore': int(m.groups()[5]),
                    'obsidian': int(m.groups()[6]),
                },
            }
            blueprints.append(BluePrint(id, costs))
    return blueprints


def part1(filename):
    initial_state = State()
    initial_state.robots['ore'] = 1
    blueprints = load(filename)
    score = 0
    for bp in blueprints:
        geodes = most_geodes(bp, initial_state)
        print(bp.id, geodes)
        score += bp.id * geodes
    return score


def part2(filename):
    return 0


# assert part1(local_file('example.txt')) == 33
print(part1(local_file('input.txt')))

# assert part2(local_file('example.txt')) == 301
print(part2(local_file('input.txt')))
