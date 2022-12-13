from string import ascii_lowercase
from collections import deque

DEFAULT_INPUT = 'day12.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    grid = {}
    with open(loc) as f:
        for y, line in enumerate(f.readlines()):
            for x, cell in enumerate(line.strip()):
                if cell == 'S':
                    start = (x, y)
                    grid[(x, y)] = 0
                elif cell == 'E':
                    goal = (x, y)
                    grid[(x, y)] = 25
                else:
                    grid[(x, y)] = ascii_lowercase.index(cell)
    seen = {start}
    d = deque([(0, start)])
    while d:
        steps, current = d.popleft()
        for adj in adjacent(*current):
            if adj in grid and adj not in seen and grid[adj] <= (grid[current] + 1):
                seen.add(adj)
                if adj == goal:
                    return steps + 1
                d.append((steps + 1, adj))

def adjacent(x: int, y: int) -> list[tuple[int, int]]:
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

def part_2(loc: str = DEFAULT_INPUT) -> int:
    grid = {}
    with open(loc) as f:
        for y, line in enumerate(f.readlines()):
            for x, cell in enumerate(line.strip()):
                if cell == 'S':
                    grid[(x, y)] = 0
                elif cell == 'E':
                    start = (x, y)
                    grid[(x, y)] = 25
                else:
                    grid[(x, y)] = ascii_lowercase.index(cell)
    seen = {start}
    d = deque([(0, start)])
    while d:
        steps, current = d.popleft()
        for adj in adjacent(*current):
            if adj in grid and adj not in seen and grid[adj] >= (grid[current] - 1):
                seen.add(adj)
                if grid[adj] == 0:
                    return steps + 1
                d.append((steps + 1, adj))

    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
