from collections import deque, defaultdict

DEFAULT_INPUT = 'day24.txt'

def day_24(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    blizzards = set()
    blizzards_at_time = defaultdict(set)
    max_x = 0
    max_y = 0
    valid = set()
    with open(loc) as f:
        for y, row in enumerate(f.readlines()):
            row = row.strip()
            max_y = max(max_y, y)
            for x, cell in enumerate(row):
                max_x = max(max_x, x)
                if cell == '<':
                    blizzards.add((x, y, -1, 0))
                    blizzards_at_time[0].add((x, y))
                if cell == '>':
                    blizzards.add((x, y, 1, 0))
                    blizzards_at_time[0].add((x, y))
                if cell == 'v':
                    blizzards.add((x, y, 0, 1))
                    blizzards_at_time[0].add((x, y))
                if cell == '^':
                    blizzards.add((x, y, 0, -1))
                    blizzards_at_time[0].add((x, y))
                if cell != '#':
                    valid.add((x, y))
    start = (1, 0)
    end = (max_x - 1, max_y)
    cycle = (max_x - 1) * (max_y - 1)
    for i in range(1, cycle):
        new_blizzards = set()
        for x, y, dx, dy in blizzards:
            x += dx
            y += dy
            if x == 0:
                x = max_x - 1
            elif x == max_x:
                x = 1
            elif y == 0:
                y = max_y - 1
            elif y == max_y:
                y = 1
            new_blizzards.add((x, y, dx, dy))
            blizzards_at_time[i].add((x, y))
        blizzards = new_blizzards
    trip_1_time = find_shortest_path(0, start, end, valid, blizzards_at_time, cycle)
    trip_2_time = find_shortest_path(trip_1_time, end, start, valid, blizzards_at_time, cycle)
    trip_3_time = find_shortest_path(trip_2_time, start, end, valid, blizzards_at_time, cycle)
    return trip_1_time, trip_3_time

def find_shortest_path(starting_time: int, start: tuple[int, int], end: tuple[int, int],
                       valid: set[tuple[int, int]], blizzards_at_time: dict[int, set[tuple[int, int]]],
                       cycle: int) -> int:
    seen = {(start, starting_time)}
    d = deque([(start, starting_time)])
    while d:
        current, time = d.popleft()
        x, y = current
        blizzards = blizzards_at_time[(time + 1) % cycle]
        adjacents = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for adj in adjacents:
            if adj in valid and adj not in blizzards and (adj, time + 1) not in seen:
                if adj == end:
                    return time + 1
                seen.add((adj, time + 1))
                d.append((adj, time + 1))
        if current not in blizzards and (current, time + 1) not in seen:
            seen.add((current, time + 1))
            d.append((current, time + 1))

    
if __name__ == '__main__':
    part_1, part_2 = day_24()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
