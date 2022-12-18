from collections import Counter, defaultdict
from enum import Enum

DEFAULT_INPUT = 'day17.txt'

class Cell(Enum):
    AIR = 1
    ROCK = 2

def day_17(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    grid = defaultdict(lambda: Cell.AIR)
    states = defaultdict(list)
    cycles = Counter()
    floor_heights = {}
    for n in range(7):
        grid[(n, -1)] = Cell.ROCK
    with open(loc) as f:
        movements = f.readline().strip()
    i = 0
    for rock_num in range(2022):
        floor_height = max((k for k, v in grid.items() if v == Cell.ROCK), key=lambda p: p[1])[1]
        rn = rock_num % 5
        rock = next_rock(rn, floor_height)
        can_drop = True
        while can_drop:
            next_movement = movements[i]
            if next_movement == '>':
                if all(point[0] < 6 for point in rock) and \
                   not any(grid[(point[0] + 1, point[1])] == Cell.ROCK for point in rock):
                    rock = [(point[0] + 1, point[1]) for point in rock]
            else:
                if all(point[0] > 0 for point in rock) and \
                   not any(grid[(point[0] - 1, point[1])] == Cell.ROCK for point in rock):
                    rock = [(point[0] - 1, point[1]) for point in rock]
            i += 1
            i %= len(movements)
            if any(grid[(point[0], point[1] - 1)] == Cell.ROCK for point in rock):
                for point in rock:
                    grid[point] = Cell.ROCK
                can_drop = False
            else:
                rock = [(point[0], point[1] - 1) for point in rock]
        states[(rn, i)].append((rock_num, floor_height))
        floor_heights[rock_num] = floor_height
    for k, v in states.items():
        if len(v) > 1:
            cycle_length = v[1][0] - v[0][0]
            cycle_height = v[1][1] - v[0][1]
            cycles[(cycle_length, cycle_height)] += 1
    cycle_length, cycle_height = cycles.most_common(1)[0][0]
    cycle_start = 1000000000000 % cycle_length
    num_cycles = 1000000000000 // cycle_length
    return max((k for k, v in grid.items() if v == Cell.ROCK), key=lambda p: p[1])[1] + 1, \
           floor_heights[cycle_start] + cycle_height * num_cycles + 1

def next_rock(rock_num: int, floor_height: int) -> list[tuple[int, int]]:
    if rock_num == 0:
        rock = [(2, 4 + floor_height), (3, 4 + floor_height), (4, 4 + floor_height),
                (5, 4 + floor_height)]
    elif rock_num == 1:
        rock = [(2, 5 + floor_height), (3, 4 + floor_height), (3, 5 + floor_height),
                (3, 6 + floor_height), (4, 5 + floor_height)]
    elif rock_num == 2:
        rock = [(2, 4 + floor_height), (3, 4 + floor_height), (4, 4 + floor_height),
                (4, 5 + floor_height), (4, 6 + floor_height)]
    elif rock_num == 3:
        rock = [(2, 4 + floor_height), (2, 5 + floor_height), (2, 6 + floor_height),
                (2, 7 + floor_height)]
    else:
        rock = [(2, 4 + floor_height), (3, 4 + floor_height), (2, 5 + floor_height),
                (3, 5 + floor_height)]
    return rock


if __name__ == '__main__':
    part_1, part_2 = day_17()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
