from collections import defaultdict
from enum import Enum

DEFAULT_INPUT = 'day14.txt'

class Cell(Enum):
    AIR = 1
    ROCK = 2
    SAND = 3

def part_1(loc: str = DEFAULT_INPUT) -> int:
    grid = defaultdict(lambda: Cell.AIR)
    with open(loc) as f:
        for line in f.readlines():
            coords = line.strip().split(' -> ')
            for start, end in zip(coords, coords[1:]):
                start_x, start_y = map(int, start.split(','))
                end_x, end_y = map(int, end.split(','))
                if start_x == end_x:
                    for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
                        grid[(start_x, y)] = Cell.ROCK
                if start_y == end_y:
                    for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
                        grid[(x, start_y)] = Cell.ROCK
    bottom = max(grid.keys(), key=lambda point:point[1])[1]
    while True:
        can_add_sand = add_sand(grid, bottom)
        if not can_add_sand:
            return len([value for value in grid.values() if value == Cell.SAND])

def add_sand(grid: dict[tuple[int, int], Cell], bottom: int) -> bool:
    sand_x, sand_y = 500, 0
    while True:
        if sand_y == bottom:
            return False
        elif grid[(sand_x, sand_y + 1)] == Cell.AIR:
            sand_y += 1
        elif grid[(sand_x - 1, sand_y + 1)] == Cell.AIR:
            sand_x -= 1
            sand_y += 1
        elif grid[(sand_x + 1, sand_y + 1)] == Cell.AIR:
            sand_x += 1
            sand_y += 1
        else:
            grid[(sand_x, sand_y)] = Cell.SAND
            return True
    
def part_2(loc: str = DEFAULT_INPUT) -> int:
    grid = defaultdict(lambda: Cell.AIR)
    with open(loc) as f:
        for line in f.readlines():
            coords = line.strip().split(' -> ')
            for start, end in zip(coords, coords[1:]):
                start_x, start_y = map(int, start.split(','))
                end_x, end_y = map(int, end.split(','))
                if start_x == end_x:
                    for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
                        grid[(start_x, y)] = Cell.ROCK
                if start_y == end_y:
                    for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
                        grid[(x, start_y)] = Cell.ROCK
    floor = max(grid.keys(), key=lambda point:point[1])[1] + 2
    while True:
        can_add_sand = add_sand_floor(grid, floor)
        if grid[(500, 0)] == Cell.SAND:
            return len([value for value in grid.values() if value == Cell.SAND])

def add_sand_floor(grid: dict[tuple[int, int], Cell], floor: int) -> bool:
    sand_x, sand_y = 500, 0
    while True:
        if sand_y == floor - 1:
            grid[(sand_x - 1, floor)] = Cell.ROCK
            grid[(sand_x, floor)] = Cell.ROCK
            grid[(sand_x + 1, floor)] = Cell.ROCK
        if grid[(sand_x, sand_y + 1)] == Cell.AIR:
            sand_y += 1
        elif grid[(sand_x - 1, sand_y + 1)] == Cell.AIR:
            sand_x -= 1
            sand_y += 1
        elif grid[(sand_x + 1, sand_y + 1)] == Cell.AIR:
            sand_x += 1
            sand_y += 1
        else:
            grid[(sand_x, sand_y)] = Cell.SAND
            return True

    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
