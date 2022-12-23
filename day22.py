from enum import Enum

DEFAULT_INPUT = 'day22.txt'

class Cell(Enum):
    TILE = 1
    WALL = 2

def part_1(loc: str = DEFAULT_INPUT) -> int:
    grid = {}
    with open(loc) as f:
        board, moves_raw = f.read().rstrip().split('\n\n')
        for y, row in enumerate(board.split('\n')):
            for x, cell in enumerate(row.rstrip()):
                if cell in '.#':
                    grid[(x, y)] = Cell.TILE if cell == '.' else Cell.WALL
    x, y = min((point for point in grid if point[1] == 0 and grid[point] == Cell.TILE),
               key = lambda point:point[0])
    dx, dy = 1, 0
    moves = []
    m = ''
    for char in moves_raw:
        if char in 'RL':
            moves.append(int(m))
            moves.append(char)
            m = ''
        else:
            m += char
    if m:
        moves.append(int(m))
    for move in moves:
        if move == 'R':
            dx, dy = -dy, dx
        elif move == 'L':
            dx, dy = dy, -dx
        else:
            for _ in range(move):
                next_x = x + dx
                next_y = y + dy
                if (next_x, next_y) not in grid:
                    if dx == 1:
                        next_x, next_y = min((point for point in grid if point[1] == y),
                                             key = lambda point:point[0])
                    elif dx == -1:
                        next_x, next_y = max((point for point in grid if point[1] == y),
                                             key = lambda point:point[0])
                    elif dy == 1:
                        next_x, next_y = min((point for point in grid if point[0] == x),
                                             key = lambda point:point[1])
                    else:
                        next_x, next_y = max((point for point in grid if point[0] == x),
                                             key = lambda point:point[1])
                if grid[(next_x, next_y)] == Cell.TILE:
                    x, y = next_x, next_y
                else:
                    break
    return 1000 * (y + 1) + 4 * (x + 1) + {(1, 0): 0, (0, 1): 1, (-1, 0): 2, (0, -1): 3}[(dx, dy)]
                

'''
 AB
 C
DE
F
'''
    
def part_2(loc: str = DEFAULT_INPUT) -> int:
    grid = {}
    with open(loc) as f:
        board, moves_raw = f.read().rstrip().split('\n\n')
        for y, row in enumerate(board.split('\n')):
            for x, cell in enumerate(row.rstrip()):
                if cell in '.#':
                    if 50 <= x < 100 and 0 <= y < 50:
                        face = 'A'
                    if 100 <= x < 150 and 0 <= y < 50:
                        face = 'B'
                    if 50 <= x < 100 and 50 <= y < 100:
                        face = 'C'
                    if 0 <= x < 50 and 100 <= y < 150:
                        face = 'D'
                    if 50 <= x < 100 and 100 <= y < 150:
                        face = 'E'
                    if 0 <= x < 50 and 150 <= y < 200:
                        face = 'F'
                    grid[(x % 50, y % 50, face)] = Cell.TILE if cell == '.' else Cell.WALL
    x, y, face = min((point for point in grid if point[1] == 0 and point[2] == 'A' and grid[point] == Cell.TILE),
                     key = lambda point:point[0])
    dx, dy = 1, 0
    moves = []
    m = ''
    for char in moves_raw:
        if char in 'RL':
            moves.append(int(m))
            moves.append(char)
            m = ''
        else:
            m += char
    if m:
        moves.append(int(m))
    for move in moves:
        if move == 'R':
            dx, dy = -dy, dx
        elif move == 'L':
            dx, dy = dy, -dx
        else:
            for _ in range(move):
                next_x = x + dx
                next_y = y + dy
                next_face = face
                next_dx = dx
                next_dy = dy
                if (next_x, next_y, face) not in grid:
                    if face == 'A':
                        if dx == 1:
                            next_x = 0
                            next_face = 'B'
                        elif dx == -1:
                            next_x = 0
                            next_y = 49 - y
                            next_face = 'D'
                            next_dx = 1
                        elif dy == 1:
                            next_y = 0
                            next_face = 'C'
                        else:
                            next_x = 0
                            next_y = x
                            next_face = 'F'
                            next_dx = 1
                            next_dy = 0
                    elif face == 'B':
                        if dx == 1:
                            next_x = 49
                            next_y = 49 - y
                            next_face = 'E'
                            next_dx = -1
                        elif dx == -1:
                            next_x = 49
                            next_face = 'A'
                        elif dy == 1:
                            next_x = 49
                            next_y = x
                            next_face = 'C'
                            next_dx = -1
                            next_dy = 0
                        else:
                            next_y = 49
                            next_face = 'F'
                    elif face == 'C':
                        if dx == 1:
                            next_x = y
                            next_y = 49
                            next_face = 'B'
                            next_dx = 0
                            next_dy = -1
                        elif dx == -1:
                            next_x = y
                            next_y = 0
                            next_face = 'D'
                            next_dx = 0
                            next_dy = 1
                        elif dy == 1:
                            next_y = 0
                            next_face = 'E'
                        else:
                            next_y = 49
                            next_face = 'A'
                    elif face == 'D':
                        if dx == 1:
                            next_x = 0
                            next_face = 'E'
                        elif dx == -1:
                            next_x = 0
                            next_y = 49 - y
                            next_face = 'A'
                            next_dx = 1
                        elif dy == 1:
                            next_y = 0
                            next_face = 'F'
                        else:
                            next_x = 0
                            next_y = x
                            next_face = 'C'
                            next_dx = 1
                            next_dy = 0
                    elif face == 'E':
                        if dx == 1:
                            next_x = 49
                            next_y = 49 - y
                            next_face = 'B'
                            next_dx = -1
                        elif dx == -1:
                            next_x = 49
                            next_face = 'D'
                        elif dy == 1:
                            next_x = 49
                            next_y = x
                            next_face = 'F'
                            next_dx = -1
                            next_dy = 0
                        else:
                            next_y = 49
                            next_face = 'C'
                    else:
                        if dx == 1:
                            next_x = y
                            next_y = 49
                            next_face = 'E'
                            next_dx = 0
                            next_dy = -1
                        elif dx == -1:
                            next_x = y
                            next_y = 0
                            next_face = 'A'
                            next_dx = 0
                            next_dy = 1
                        elif dy == 1:
                            next_y = 0
                            next_face = 'B'
                        else:
                            next_y = 49
                            next_face = 'D'
                if grid[(next_x, next_y, next_face)] == Cell.TILE:
                    x, y, face, dx, dy = next_x, next_y, next_face, next_dx, next_dy
                else:
                    break
    if face == 'A':
        x += 50
    elif face == 'B':
        x += 100
    elif face == 'C':
        x += 50
        y += 50
    elif face == 'D':
        y += 100
    elif face == 'E':
        x += 50
        y += 100
    else:
        y += 150
    return 1000 * (y + 1) + 4 * (x + 1) + {(1, 0): 0, (0, 1): 1, (-1, 0): 2, (0, -1): 3}[(dx, dy)]
                    

    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
