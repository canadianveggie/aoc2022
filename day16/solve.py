import itertools
import os
import networkx as nx
import re


def local_file(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


def load_valves(filename):
    graph = nx.Graph()
    valves = dict()
    with open(filename) as f:
        for line in f.readlines():
            m = re.match(r"Valve (\w+) has flow rate=(\d+); tunnel(s?) lead(s?) to valve(s?) (.*)", line)
            valve_name = m.groups()[0]
            rate = int(m.groups()[1])
            adjacents = m.groups()[5].split(", ")
            for adjacent in adjacents:
                graph.add_edge(valve_name, adjacent)
            if rate > 0:
                valves[valve_name] = rate
    return (graph, valves)


def find_max_path(graph, valve_flows, valves_on=set(), start='AA', max_steps=30):
    best_path = []
    best_flow = 0
    for valve in set(valve_flows.keys()) - valves_on:
        cost = len(nx.shortest_path(graph, start, valve))
        # print(f'{start} to {valve} costs {cost}')
        if cost <= max_steps:
            cost_remainder = max_steps - cost
            if cost_remainder > 0:
                (sub_best_path, sub_best_flow) = find_max_path(graph, valve_flows, valves_on | {valve}, valve, cost_remainder)
            else:
                sub_best_path = []
                sub_best_flow = 0
            extra_flow = (max_steps - cost) * valve_flows[valve] + sub_best_flow

            if extra_flow > best_flow:
                best_flow = extra_flow
                best_path = [valve] + sub_best_path

    # print(f'best from {start} in {max_steps} steps is {best_path} = {best_flow}')
    return (best_path, best_flow)



def find_double_path(graph, valve_flows, valves_on=set(), start1='AA', start2='AA', max_steps1=26, max_steps2=26):
    

    all_paths = itertools.permutations(valve_flows.keys())

    best_flow = 0
    for valve1 in set(valve_flows.keys()) - valves_on:
        cost1 = len(nx.shortest_path(graph, start1, valve1))
        if cost1 <= max_steps1:
            remaining_valves = set(valve_flows.keys()) - valves_on - {valve1}
            if len(remaining_valves) == 0:
                remaining_valves = {None}
            for valve2 in remaining_valves:
                if valve2 is None:
                    cost2 = 0
                else:
                    cost2 = len(nx.shortest_path(graph, start2, valve2))

                if cost2 <= max_steps2:
                    cost_remainder1 = max_steps1 - cost1
                    cost_remainder2 = max_steps2 - cost2
                    
                    sub_best_flow = find_double_path(graph, valve_flows, valves_on | {valve1} | {valve2}, valve1, valve2, cost_remainder1, cost_remainder2)
                    extra_flow = (max_steps1 - cost1) * valve_flows[valve1] + (max_steps2 - cost2) * valve_flows[valve2] + sub_best_flow

                    if extra_flow > best_flow:
                        best_flow = extra_flow

    print(f'best from {start1} and {start2} in {max_steps1} and {max_steps2} steps = {best_flow}')
    return best_flow


def part1(filename):
    (graph, valves) = load_valves(filename)
    (max_path, max_flow) = find_max_path(graph, valves)
    print(max_path)
    print(max_flow)
    return max_flow


def part2(filename):
    (graph, valves) = load_valves(filename)
    all_paths = itertools.permutations(valves.keys())
    print(len(list(all_paths)))

    max_flow = find_double_path(graph, valves)
    print(max_flow)
    return max_flow


assert part1(local_file('example.txt')) == 1651
# print(part1(local_file('input.txt')))

assert part2(local_file('example.txt')) == 1707
print(part2(local_file('input.txt')))
