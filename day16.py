from collections import deque
from itertools import combinations

DEFAULT_INPUT = 'day16.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
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
    start = (0, 30, 'AA', frozenset())
    seen = {(0, 'AA', frozenset())}
    max_pressure = 0
    d = deque([start])
    while d:
        pressure, time, location, open_valves = d.popleft()
        if time <= 0:
            continue
        if flow_rates[location] and location not in open_valves:
            new_pressure = pressure + flow_rates[location] * (time - 1)
            max_pressure = max(max_pressure, new_pressure)
            d.append((new_pressure, time - 1, location, open_valves | frozenset([location])))
            seen.add((new_pressure, location, open_valves | frozenset([location])))
        for node, distance in graph[location].items():
            if (pressure, node, open_valves) not in seen:
                d.append((pressure, time - distance, node, open_valves))
                seen.add((pressure, node, open_valves))
    return max_pressure

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

def part_2(loc: str = DEFAULT_INPUT) -> int:
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
    start = (0, 26, 'AA', frozenset())
    seen = {(0, 'AA', frozenset())}
    pressure_states = {(0, frozenset())}
    d = deque([start])
    while d:
        pressure, time, location, open_valves = d.popleft()
        if time <= 0:
            continue
        if flow_rates[location] and location not in open_valves:
            new_pressure = pressure + flow_rates[location] * (time - 1)
            d.append((new_pressure, time - 1, location, open_valves | frozenset([location])))
            seen.add((new_pressure, location, open_valves | frozenset([location])))
            pressure_states.add((new_pressure, open_valves | frozenset([location])))
        for node, distance in graph[location].items():
            if (pressure, node, open_valves) not in seen:
                d.append((pressure, time - distance, node, open_valves))
                seen.add((pressure, node, open_valves))
    max_pressure = 0
    for state_a, state_b in combinations(pressure_states, 2):
        pressure_a, valves_a = state_a
        pressure_b, valves_b = state_b
        if not valves_a & valves_b:
            max_pressure = max(max_pressure, pressure_a + pressure_b)
    return max_pressure

    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
