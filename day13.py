from functools import cmp_to_key

DEFAULT_INPUT = 'day13.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        pairs = [packets.split('\n') for packets in f.read().split('\n\n')]
    for pair in pairs:
        pair[0] = eval(pair[0])
        pair[1] = eval(pair[1])
    return sum(i + 1 for i, pair in enumerate(pairs) if in_order(*pair) == -1)

def in_order(left: list, right: list) -> int:
    i = 0
    while True:
        if i == len(left) == len(right):
            return 0
        if i == len(left):
            return -1
        if i == len(right):
            return 1
        left_current = left[i]
        right_current = right[i]
        if isinstance(left_current, int) and isinstance(right_current, int):
            if left_current == right_current:
                i += 1
            else:
                return -1 if left_current < right_current else 1
        else:
            if isinstance(left_current, int):
                left_current = [left_current]
            if isinstance(right_current, int):
                right_current = [right_current]
            correct_order = in_order(left_current, right_current)
            if correct_order in (1, -1):
                return correct_order
            i += 1
    
def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        lines = [eval(line.strip()) for line in f.readlines() if line != '\n']
    lines.append([[2]])
    lines.append([[6]])
    lines.sort(key=cmp_to_key(in_order))
    return (lines.index([[2]]) + 1) * (lines.index([[6]]) + 1)

    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
