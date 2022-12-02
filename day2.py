DEFAULT_INPUT = 'day2.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    shape_points = {'X': 1, 'Y': 2, 'Z': 3}
    outcome_points = {'X': {'A': 3, 'B': 0, 'C': 6},
                      'Y': {'A': 6, 'B': 3, 'C': 0},
                      'Z': {'A': 0, 'B': 6, 'C': 3}}
    with open(loc) as f:
        return sum(shape_points[line[2]] + outcome_points[line[2]][line[0]]
                   for line in f.readlines())
            
def part_2(loc: str = DEFAULT_INPUT) -> int:
    outcome_points = {'X': 0, 'Y': 3, 'Z': 6}
    shape_points = {'X': {'A': 3, 'B': 1, 'C': 2},
                    'Y': {'A': 1, 'B': 2, 'C': 3},
                    'Z': {'A': 2, 'B': 3, 'C': 1}}
    with open(loc) as f:
        return sum(outcome_points[line[2]] + shape_points[line[2]][line[0]]
                   for line in f.readlines())

    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
