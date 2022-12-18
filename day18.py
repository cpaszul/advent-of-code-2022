from collections import deque
from itertools import combinations

DEFAULT_INPUT = 'day18.txt'

def day_18(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    with open(loc) as f:
        cubes = [tuple(map(int, line.strip().split(','))) for line in f.readlines()]
    cube_adjs = adjacent_surfaces(cubes)
    cube_surface_area = 6 * len(cubes) - 2 * cube_adjs
    min_x = min(cubes, key=lambda p:p[0])[0] - 1
    min_y = min(cubes, key=lambda p:p[1])[1] - 1
    min_z = min(cubes, key=lambda p:p[2])[2] - 1
    max_x = max(cubes, key=lambda p:p[0])[0] + 1
    max_y = max(cubes, key=lambda p:p[1])[1] + 1
    max_z = max(cubes, key=lambda p:p[2])[2] + 1
    exterior_air = {(min_x, min_y, min_z)}
    d = deque([(min_x, min_y, min_z)])
    while d:
        current = d.popleft()
        adjs = adjacent_cubes(*current)
        for adj in adjs:
            if min_x <= adj[0] <= max_x and min_y <= adj[1] <= max_y and \
               min_z <= adj[2] <= max_z and adj not in exterior_air and adj not in cubes:
                exterior_air.add(adj)
                d.append(adj)
    interior_air = []
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            for z in range(min_z, max_z + 1):
                if (x, y, z) not in cubes and (x, y, z) not in exterior_air:
                    interior_air.append((x, y, z))
    interior_adjs = adjacent_surfaces(interior_air)
    interior_surface_area = 6 * len(interior_air) - 2 * interior_adjs
    return cube_surface_area, cube_surface_area - interior_surface_area

def adjacent_surfaces(cubes: list[tuple[int, int, int]]) -> int:
    adjs = 0
    for cube_a, cube_b in combinations(cubes, 2):
        x_a, y_a, z_a = cube_a
        x_b, y_b, z_b = cube_b
        if x_a == x_b and y_a == y_b and abs(z_a - z_b) == 1:
            adjs += 1
        if x_a == x_b and abs(y_a - y_b) == 1 and z_a == z_b:
            adjs += 1
        if abs(x_a - x_b) == 1 and y_a == y_b and z_a == z_b:
            adjs += 1
    return adjs

def adjacent_cubes(x: int, y: int, z: int) -> list[tuple[int, int, int]]:
    return [(x + 1, y, z), (x, y + 1, z), (x, y, z + 1),
            (x - 1, y, z), (x, y - 1, z), (x, y, z - 1)]
        

if __name__ == '__main__':
    part_1, part_2 = day_18()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
