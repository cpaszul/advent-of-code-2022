from collections import Counter, deque

DEFAULT_INPUT = 'day23.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    proposals = deque(['N', 'S', 'W', 'E'])
    directs = {'N': ((-1, -1), (0, -1), (1, -1)),
               'S': ((-1, 1), (0, 1), (1, 1)),
               'E': ((1, -1), (1, 0), (1, 1)),
               'W': ((-1, -1), (-1, 0), (-1, 1))}
    elves = set()
    with open(loc) as f:
        for y, row in enumerate(f.readlines()):
            for x, cell in enumerate(row.strip()):
                if cell == '#':
                    elves.add((x, y))
    for _ in range(10):
        new_elves = set()
        moves = {}
        move_counter = Counter()
        for elf in elves:
            x, y = elf
            adjs = adjacent(x, y)
            if not any(adj in elves for adj in adjs):
                moves[elf] = elf
                move_counter[elf] += 1
            else:
                i = 0
                decided = False
                while i < 4 and not decided:
                    proposed = proposals[i]
                    adjs = [(x + dx, y + dy) for dx, dy in directs[proposed]]
                    if not any(adj in elves for adj in adjs):
                        moves[elf] = adjs[1]
                        move_counter[adjs[1]] += 1
                        decided = True
                    i += 1
                if not decided:
                    moves[elf] = elf
                    move_counter[elf] += 1
        for start, end in moves.items():
            if move_counter[end] > 1:
                new_elves.add(start)
            else:
                new_elves.add(end)
        elves = new_elves
        proposals.rotate(-1)
    min_x = min(elves, key=lambda point:point[0])[0]
    min_y = min(elves, key=lambda point:point[1])[1]
    max_x = max(elves, key=lambda point:point[0])[0]
    max_y = max(elves, key=lambda point:point[1])[1]
    return sum((x, y) not in elves for x in range(min_x, max_x + 1) for y in range(min_y, max_y + 1))

def adjacent(x: int, y: int) -> list[tuple[int, int]]:
    return [(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2) if not (i == j == 0)]
    
def part_2(loc: str = DEFAULT_INPUT) -> int:
    proposals = deque(['N', 'S', 'W', 'E'])
    directs = {'N': ((-1, -1), (0, -1), (1, -1)),
               'S': ((-1, 1), (0, 1), (1, 1)),
               'E': ((1, -1), (1, 0), (1, 1)),
               'W': ((-1, -1), (-1, 0), (-1, 1))}
    elves = set()
    with open(loc) as f:
        for y, row in enumerate(f.readlines()):
            for x, cell in enumerate(row.strip()):
                if cell == '#':
                    elves.add((x, y))
    n = 1
    while True:
        new_elves = set()
        moves = {}
        move_counter = Counter()
        for elf in elves:
            x, y = elf
            adjs = adjacent(x, y)
            if not any(adj in elves for adj in adjs):
                moves[elf] = elf
                move_counter[elf] += 1
            else:
                i = 0
                decided = False
                while i < 4 and not decided:
                    proposed = proposals[i]
                    adjs = [(x + dx, y + dy) for dx, dy in directs[proposed]]
                    if not any(adj in elves for adj in adjs):
                        moves[elf] = adjs[1]
                        move_counter[adjs[1]] += 1
                        decided = True
                    i += 1
                if not decided:
                    moves[elf] = elf
                    move_counter[elf] += 1
        for start, end in moves.items():
            if move_counter[end] > 1:
                new_elves.add(start)
            else:
                new_elves.add(end)
        if elves == new_elves:
            return n
        elves = new_elves
        proposals.rotate(-1)
        n += 1

    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
