import re

DEFAULT_INPUT = 'day15.txt'

def day_15(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    sensor_distances = {}
    with open(loc) as f:
        for line in f.readlines():
            m = re.match(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
            sensor = int(m.group(1)), int(m.group(2))
            beacon = int(m.group(3)), int(m.group(4))
            sensor_distances[sensor] = distance(sensor, beacon)
    part_1_res = sum(r[1] - r[0] for r in get_invalid_ranges(sensor_distances, 2000000))
    for y in range(4000001):
        ranges = get_invalid_ranges(sensor_distances, y)
        valid_row = True
        for r in ranges:
            if r[0] <= 0 and r[1] >= 4000000:
                valid_row = False
        if valid_row:
            for r in ranges:
                if r[0] <= 0 and r[1] >= 0:
                    return part_1_res, (r[1] + 1) * 4000000 + y

def distance(point_1: tuple[int, int], point_2: tuple[int, int]) -> int:
    return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])

def get_invalid_ranges(sensor_distances: dict[tuple[int, int], int], y: int) -> list[list[int]]:
    ranges = []
    for sensor, dist in sensor_distances.items():
        if abs(y - sensor[1]) < dist:
            n = dist - abs(y - sensor[1])
            ranges.append([sensor[0] - n, sensor[0] + n])
    ranges.sort(key=lambda point:point[0])
    i = 0
    while i < len(ranges) - 1:
        if ranges[i][1] + 1 >= ranges[i + 1][0]:
            ranges[i][1] = max(ranges[i][1], ranges[i + 1][1])
            ranges.pop(i + 1)
            continue
        i += 1
    return ranges

    
if __name__ == '__main__':
    part_1, part_2 = day_15()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
