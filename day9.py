DEFAULT_INPUT = 'day9.txt'

def day_9(loc: str = DEFAULT_INPUT) -> int:
    one_positions = {(0, 0)}
    nine_positions = {(0, 0)}
    directions = {'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1)}
    with open(loc) as f:
        moves = [line.strip() for line in f.readlines()]
    head = 0, 0
    one = 0, 0
    two = 0, 0
    three = 0, 0
    four = 0, 0
    five = 0, 0
    six = 0, 0
    seven = 0, 0
    eight = 0, 0
    nine = 0, 0
    for move in moves:
        direction, n = move.split(' ')
        n = int(n)
        for _ in range(n):
            head = head[0] + directions[direction][0], \
                   head[1] + directions[direction][1],
            one = update_tail(head, one)
            two = update_tail(one, two)
            three = update_tail(two, three)
            four = update_tail(three, four)
            five = update_tail(four, five)
            six = update_tail(five, six)
            seven = update_tail(six, seven)
            eight = update_tail(seven, eight)
            nine = update_tail(eight, nine)
            one_positions.add(one)
            nine_positions.add(nine)
    return len(one_positions), len(nine_positions)

def update_tail(head: tuple[int, int], tail: tuple[int, int]) -> tuple[int, int]:
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]
    x_direction = 0
    y_direction = 0
    if abs(dx) > 1 or abs(dy) > 1:
        if head[0] > tail[0]:
            x_direction = 1
        if head[0] < tail[0]:
            x_direction = -1
        if head[1] > tail[1]:
            y_direction = 1
        if head[1] < tail[1]:
            y_direction = -1
    return tail[0] + x_direction, tail[1] + y_direction

    
if __name__ == '__main__':
    part_1, part_2 = day_9()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
