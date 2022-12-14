import os
import networkx as nx


def local_file(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


def calc_height(letter):
    if letter == 'S':
        return ord('a')
    elif letter == 'E':
        return ord('z')
    else:
        return ord(letter)

def parse_input(filename):
    start = (0,0)
    end = (0,0)
    grid = []
    with open(filename) as f:
        for line in f.readlines():
            grid.append([x for x in line.strip()])

    graph = nx.DiGraph()
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            letter = grid[x][y]
            graph.add_node((x, y), letter=letter)
            if letter == 'S':
                start = (x, y)
            elif letter == 'E':
                end = (x, y)

            height = calc_height(letter)

            adjacents = []

            if x-1 >= 0:
                adjacents.append((x-1, y))
            if x+1 < len(grid):
                adjacents.append((x+1, y))
            if y-1 >= 0:
                adjacents.append((x, y-1))
            if y+1 < len(grid[x]):
                adjacents.append((x, y+1))

            for adj in adjacents:
                height_delta = calc_height(grid[adj[0]][adj[1]]) - height
                if height_delta <= 1:
                    graph.add_edge((x,y), adj)

    return (graph, start, end)


def part1(filename):
    (graph, start, end) = parse_input(filename)

    shortest_path = nx.shortest_path(graph, start, end)
    return len(shortest_path) - 1


def part2(filename):
    (graph, start, end) = parse_input(filename)

    possible_starts = [n[0] for n in graph.nodes(data=True) if n[1]["letter"] == 'a'] 
    min_distance = 99999999999999999
    for p_start in possible_starts:
        try:
            shortest_path = nx.shortest_path(graph, p_start, end)
            min_distance = min(min_distance, len(shortest_path) - 1)
        except Exception:
            pass
    return min_distance


assert part1(local_file('example.txt')) == 31
print(part1(local_file('input.txt')))


assert part2(local_file('example.txt')) == 29
print(part2(local_file('input.txt')))

