import os


def local_file(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


def load(filename):
    elves = set()
    with open(filename) as f:
        lines = f.readlines()
        for row_i in range(len(lines)):
            line = lines[row_i]
            for col_j in range(len(line.strip())):
                col = line[col_j]
                if col == '#':
                    elves.add((row_i, col_j))
    return elves


def find_adjacents(coord):
    return {
        'NW': (coord[0] - 1, coord[1] - 1),
         'N': (coord[0] - 1, coord[1]    ),
        'NE': (coord[0] - 1, coord[1] + 1),
        'E':  (coord[0],     coord[1] + 1),
        'SE': (coord[0] + 1, coord[1] + 1),
         'S': (coord[0] + 1, coord[1]    ),
        'SW': (coord[0] + 1, coord[1] - 1),
         'W': (coord[0]    , coord[1] - 1),
    }


def move(elves, directions):
    next_positions = dict() # reverse dictionary
    contested_positions = set()
    for elf in elves:
        adjacents = find_adjacents(elf)
        # if I have a neighbour, find a move
        if any([a in elves for a in adjacents.values()]):
            # find the first direction that is 'free'
            found_a_move = False
            for direction in directions:
                direction_coords = [a[1] for a in adjacents.items() if direction in a[0]]
                if not any([a in elves for a in direction_coords]):
                    found_a_move = True
                    elf_next = adjacents[direction]
                    if elf_next in contested_positions:
                        # at least 2 other elves are already fighting over this spot
                        # print(f'{elf} is not moving to {elf_next}')
                        next_positions[elf] = elf
                        break
                    elif elf_next in next_positions:
                        # 2 elves are fighting over this spot
                        contested_positions.add(elf_next)
                        # move the other elf back
                        other_elf_start = next_positions[elf_next]
                        next_positions[other_elf_start] = other_elf_start
                        del next_positions[elf_next]
                        next_positions[elf] = elf
                        # print(f'{elf} is not moving to {elf_next} and {other_elf_start} is moving back')
                    else:
                        next_positions[elf_next] = elf
                        # print(f'{elf} is moving to {elf_next}')
                    break
            if not found_a_move:
                # print(f'nothing found for {elf}')
                next_positions[elf] = elf
        else:
            # not moving
            # print(f'cant move {elf}')
            next_positions[elf] = elf

    
    return set(next_positions.keys())


def print_elves(elves):
    min_row = min([elf[0] for elf in elves])
    max_row = max([elf[0] for elf in elves])
    min_col = min([elf[1] for elf in elves])
    max_col = max([elf[1] for elf in elves])

    for i in range(min_row, max_row+1):
        for j in range(min_col, max_col+1):
            if (i,j) in elves:
                print('#', end='')
            else:
                print('.', end='')
        print('')
    print('')


def count_empty_tiles(elves):
    min_row = min([elf[0] for elf in elves])
    max_row = max([elf[0] for elf in elves])
    min_col = min([elf[1] for elf in elves])
    max_col = max([elf[1] for elf in elves])

    grid_size = (max_row - min_row + 1) * (max_col - min_col + 1)
    print(grid_size)
    return grid_size - len(elves)


def part1(filename):
    elves = load(filename)
    directions = ['N', 'S', 'W', 'E']
    # print_elves(elves)
    for i in range(10):
        elves = move(elves, directions)
        # print_elves(elves)
        # cycle directions
        directions.append(directions.pop(0))
    return count_empty_tiles(elves)


def part2(filename):
    elves = load(filename)
    directions = ['N', 'S', 'W', 'E']
    # print_elves(elves)
    i = 1
    while True:
        next_elves = move(elves, directions)
        if elves == next_elves:
            # no one moved
            return i
        elves = next_elves
        # print_elves(elves)
        # cycle directions
        directions.append(directions.pop(0))
        i += 1


part1(local_file('tiny_example.txt'))
assert part1(local_file('example.txt')) == 110
print(part1(local_file('input.txt')))

assert part2(local_file('example.txt')) == 20
print(part2(local_file('input.txt')))
