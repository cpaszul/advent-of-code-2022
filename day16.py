from collections import defaultdict, deque
from itertools import combinations

DEFAULT_INPUT = 'day16.txt'

def day_16(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    graph = {}
    flow_rates = {}
    with open(loc) as f:
        for line in f.readlines():
            left, right = line.strip().split(';')
            start = left.split(' ')[1]
            flow = int(left.split('=')[1])
            if 'valves' in right:
                ends = right.split('valves ')[1].split(', ')
            else:
                ends = [right.split('valve ')[1]]
            if flow or start == 'AA':
                flow_rates[start] = flow
            graph[start] = ends
    graph = simplify(flow_rates.keys(), graph)
    part_1_res = max(get_pressures(30, graph, flow_rates).values())
    pressures = get_pressures(26, graph, flow_rates)
    max_pressure = 0
    for valves_a, valves_b in combinations(pressures.keys(), 2):
        pressure_a = pressures[valves_a]
        pressure_b = pressures[valves_b]
        if not valves_a & valves_b:
            max_pressure = max(max_pressure, pressure_a + pressure_b)
    return part_1_res, max_pressure

def simplify(important_nodes: list[str], graph: dict[str, list[str]]) -> dict[str, dict[str, int]]:
    simple_graph = {}
    for node in important_nodes:
        simple_graph[node] = shortest_path(graph, node, important_nodes)
    return simple_graph

def shortest_path(graph:dict[str, list[str]], start: str, ends: list[str]) -> dict[str, int]:
    distances = {}
    d = deque([(0, start)])
    seen = {start}
    while d:
        dist, current = d.popleft()
        if current in ends and current != start:
            distances[current] = dist
            continue
        for node in graph[current]:
            if node not in seen:
                seen.add(node)
                d.append((dist + 1, node))
    return distances

def get_pressures(starting_time: int, graph: dict[str, dict[str, int]],
                  flow_rates: dict[str, int]) -> dict[frozenset[str], int]:
    start = (0, starting_time, 'AA', frozenset())
    seen = {(0, 'AA', frozenset())}
    pressures = defaultdict(int)
    d = deque([start])
    while d:
        pressure, time, location, open_valves = d.popleft()
        if time <= 0:
            continue
        if flow_rates[location] and location not in open_valves:
            new_pressure = pressure + flow_rates[location] * (time - 1)
            new_valves = open_valves | frozenset([location])
            if new_pressure > pressures[new_valves]:
                pressures[new_valves] = new_pressure
                d.append((new_pressure, time - 1, location, new_valves))
                seen.add((new_pressure, location, new_valves))
        for node, distance in graph[location].items():
            if (pressure, node, open_valves) not in seen:
                d.append((pressure, time - distance, node, open_valves))
                seen.add((pressure, node, open_valves))
    return pressures

    
if __name__ == '__main__':
    part_1, part_2 = day_16()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
