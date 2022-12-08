DEFAULT_INPUT = 'day8.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        grid = tuple(tuple(map(int, (char for char in line.strip()))) for line in f.readlines())
    return sum(visible(grid, x, y) for x in range(len(grid[0])) for y in range(len(grid)))

def visible(grid: tuple[tuple[int]], x: int, y: int) -> bool:
    return (x == 0 or
            all(grid[y][x] > tree for tree in (grid[y][n] for n in range(x)))) or \
           (x == len(grid[0]) - 1 or
            all(grid[y][x] > tree for tree in (grid[y][n] for n in range(x + 1, len(grid[0]))))) or \
           (y == 0 or
            all(grid[y][x] > tree for tree in (grid[n][x] for n in range(y)))) or \
           (y == len(grid) - 1 or
            all(grid[y][x] > tree for tree in (grid[n][x] for n in range(y + 1, len(grid)))))
            
def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        grid = tuple(tuple(map(int, (char for char in line.strip()))) for line in f.readlines())
    return max(score(grid, x, y) for x in range(len(grid[0])) for y in range(len(grid)))

def score(grid: tuple[tuple[int]], x: int, y: int) -> int:
    return number_visible_from_left(grid, x, y) * \
           number_visible_from_right(grid, x, y) * \
           number_visible_from_top(grid, x, y) * \
           number_visible_from_bottom(grid, x, y)

def number_visible_from_left(grid: tuple[tuple[int]], x: int, y: int) -> int:
    i = 0
    for n in range(x - 1, -1, -1):
        i += 1
        if grid[y][x] <= grid[y][n]:
            break
    return i

def number_visible_from_right(grid: tuple[tuple[int]], x: int, y: int) -> int:
    i = 0
    for n in range(x + 1, len(grid[0])):
        i += 1
        if grid[y][x] <= grid[y][n]:
            break
    return i

def number_visible_from_top(grid: tuple[tuple[int]], x: int, y: int) -> int:
    i = 0
    for n in range(y - 1, -1, -1):
        i += 1
        if grid[y][x] <= grid[n][x]:
            break
    return i

def number_visible_from_bottom(grid: tuple[tuple[int]], x: int, y: int) -> int:
    i = 0
    for n in range(y + 1, len(grid)):
        i += 1
        if grid[y][x] <= grid[n][x]:
            break
    return i

    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
