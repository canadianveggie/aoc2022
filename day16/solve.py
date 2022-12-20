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


def valve_pair_distances(graph, valves, start='AA'):
    nodes = set(valves.keys()) | {start}
    distances = dict()
    for pair in itertools.combinations(nodes, 2):
        distance = len(nx.shortest_path(graph, pair[0], pair[1]))
        distances[(pair[0], pair[1])] = distance
        distances[(pair[1], pair[0])] = distance
    return distances


def find_max_path(valve_flows, distances, valves_path=['AA'], flow=0, max_steps=30, paths_to_explore=5):
    to_expore = find_next_steps_to_explore(distances, valve_flows, set(valve_flows.keys()) - set(valves_path), valves_path[-1], max_steps, paths_to_explore)
    # print (f"{valves_path} = {flow}") if len(to_expore) == 0 # leaf node

    best_path = valves_path
    best_flow = flow
    for (valve, extra_flow, cost) in to_expore:
        # print(f"{valves_path[-1]} to {valve} gives {extra_flow} with cost {cost}")
        (sub_best_path, sub_best_flow) = find_max_path(valve_flows, distances, valves_path + [valve], flow + extra_flow, max_steps - cost, paths_to_explore)
        
        if sub_best_flow > best_flow:
            best_flow = sub_best_flow
            best_path = sub_best_path

    return (best_path, best_flow)


def find_next_steps_to_explore(distances, valve_flows, possible_valves, start, max_steps, paths_to_explore):
    possible_next_steps = []
    for valve in possible_valves:
        cost = distances[(start, valve)]
        if cost <= max_steps:
            extra_flow = (max_steps - cost) * valve_flows[valve]
            possible_next_steps.append((valve, extra_flow, cost))

    return sorted(possible_next_steps, key=lambda x:x[1], reverse=True)[:paths_to_explore]

best_so_far = 0

def find_double_path(valve_flows, distances, valves_path1=['AA'], valves_path2=['AA'], flow=0, max_steps1=26, max_steps2=26, paths_to_explore=8):
    possible_valves = set(valve_flows.keys()) - set(valves_path1) - set(valves_path2)
    to_expore1 = find_next_steps_to_explore(distances, valve_flows, possible_valves, valves_path1[-1], max_steps1, paths_to_explore)
    to_expore2 = find_next_steps_to_explore(distances, valve_flows, possible_valves, valves_path2[-1], max_steps2, paths_to_explore)

    if len(to_expore1) == 0 and len(to_expore2) == 0:
        global best_so_far
        if flow > best_so_far:
            print (f"{valves_path1} / {valves_path2} = {flow}")
            best_so_far = flow
        return (valves_path1, valves_path2, flow)

    if len(to_expore1) == 0:
        to_expore1.append((valves_path1[-1], 0, 0))
    if len(to_expore2) == 0:
        to_expore2.append((valves_path2[-1], 0, 0))

    best_path1 = valves_path1
    best_path2 = valves_path2
    best_flow = flow
    for option1, option2 in itertools.product(to_expore1, to_expore2):
        (valve1, extra_flow1, cost1) = option1
        (valve2, extra_flow2, cost2) = option2
        if valve1 == valve2:
            continue

        (sub_best_path1, sub_best_path2, sub_best_flow) = find_double_path(valve_flows,
                                                                           distances,
                                                                           valves_path1 + [valve1],
                                                                           valves_path2 + [valve2],
                                                                           flow + extra_flow1 + extra_flow2,
                                                                           max_steps1 - cost1,
                                                                           max_steps2 - cost2,
                                                                           paths_to_explore)
        
        if sub_best_flow > best_flow:
            best_flow = sub_best_flow
            best_path1 = sub_best_path1
            best_path2 = sub_best_path2

    return (best_path1, best_path2, best_flow)


def part1(filename):
    (graph, valves) = load_valves(filename)
    distances = valve_pair_distances(graph, valves)
    (max_path, max_flow) = find_max_path(valves, distances)
    print(max_path)
    print(max_flow)
    return max_flow


def part2(filename):
    (graph, valves) = load_valves(filename)
    distances = valve_pair_distances(graph, valves)
    (max_path1, max_path2, max_flow) = find_double_path(valves, distances)
    print(max_path1, max_path2)
    print(max_flow)
    return max_flow


assert part1(local_file('example.txt')) == 1651
print(part1(local_file('input.txt')))

assert part2(local_file('example.txt')) == 1707
print(part2(local_file('input.txt')))
