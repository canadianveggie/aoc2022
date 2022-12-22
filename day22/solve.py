import os
import re


def local_file(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


class Grid(object):
    def __init__(self, rows):
        self.rows = rows
        self.cursor = (0, self.rows[0].values.index('.'))
        self.facing = 'R'


    def advance(self, instruction):
        directions = ['L', 'D', 'R', 'U']
        if instruction == 'L' or instruction == 'R':
            current_direction_i = directions.index(self.facing)
            delta_direction = 1 if instruction == 'L' else -1
            next_direction_i = current_direction_i + delta_direction
            self.facing = directions[next_direction_i % len(directions)]
        else:
            steps = int(instruction)
            self.walk(steps)
            assert self.get_value(self.cursor[0], self.cursor[1]) == '.'

    def get_row(self, row_i):
        return self.rows[row_i]

    def get_col(self, col_j):
        x = Line([self.get_value(row_i, col_j) for row_i in range(len(self.rows))])
        return x

    def get_value(self, row_i, col_j):
        if 0 <= row_i < len(self.rows):
            row = self.rows[row_i]
            if 0 <= col_j < len(row.values):
                return row.values[col_j]
        return ' '


    def walk(self, steps):
        wall_encountered = False
        while steps > 0 and not wall_encountered:
            if self.facing == 'R' or self.facing == 'L':
                line = self.get_row(self.cursor[0])
                start_index = self.cursor[1]
            else:
                line = self.get_col(self.cursor[1])
                start_index = self.cursor[0]


            if self.facing == 'R' or self.facing == 'D':
                # if we're starting at the end, look at the beginning
                if start_index == line.max_index:
                    start_index = line.min_index - 1
                next_index = min(line.max_index, start_index + steps)

                # look for obstacles
                to_examine = line.values[start_index + 1:next_index + 1]
                if '#' in to_examine:
                    # found a wall
                    next_index = start_index + to_examine.index('#')
                    wall_encountered = True

            else:
                # if we're starting at the start, look at the end
                if start_index == line.min_index:
                    start_index = line.max_index + 1
                next_index = max(line.min_index, start_index - steps)

                # look for obstacles
                to_examine = line.values[next_index:start_index]
                to_examine.reverse()
                if '#' in to_examine:
                    # found a wall
                    next_index = start_index - to_examine.index('#')
                    wall_encountered = True

            
            steps_taken = abs(next_index - start_index)
            if steps_taken > 0:
                if self.facing == 'R' or self.facing == 'L':
                    self.cursor = (self.cursor[0], next_index)
                else:
                    self.cursor = (next_index, self.cursor[1])
            steps -= steps_taken


    def __str__(self):
        cursor_strs = {
            'R': '>',
            'L': '<',
            'U': '^',
            'D': 'v',
        }
        grid_str = ""
        for i in range(len(self.rows)):
            row = self.rows[i]
            for j in range(len(row.values)):
                col = row.values[j]
                if (i, j) == self.cursor:
                    col = cursor_strs[self.facing]
                grid_str += col
            grid_str += '\n'
        return grid_str


class Line(object):
    def __init__(self, row_str):
        self.values = [c for c in row_str]
        
        self.min_index = None
        self.max_index = 0
        for i in range(len(self.values)):
            if self.values[i] != ' ':
                if self.min_index is None:
                    self.min_index = i
                self.max_index = i



def load(filename):
    with open(filename) as f:
        rows = []
        while True:
            line = f.readline()
            if line.strip() != '':
                rows.append(Line(line.replace('\n', '')))
            else:
                break
        grid = Grid(rows)

        line = f.readline().strip()
        instructions = re.findall(r"\d+|L|R", line)
        return (grid, instructions)


def part1(filename):
    (grid, instructions) = load(filename)
    
    for instruction in instructions:
        print(instruction)
        grid.advance(instruction)
    
    print(grid.cursor)
    facing_values = {
        'R': 0,
        'D': 1,
        'L': 2,
        'U': 3,
    }
    facing_value = facing_values[grid.facing]
    return (grid.cursor[0] + 1) * 1000 + (grid.cursor[1] + 1) * 4 + facing_value 


def part2(filename):
    (grid, instructions) = load(filename)
    return 0


assert part1(local_file('example.txt')) == 6032
print(part1(local_file('input.txt')))

# assert part2(local_file('example.txt')) == 5031
# print(part2(local_file('input.txt')))
