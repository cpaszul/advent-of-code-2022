DEFAULT_INPUT = 'day6.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        buffer = f.readline()
        i = 0
        while True:
            section = buffer[i:i + 4]
            if all_unique(section):
                return i + 4
            i += 1

def all_unique(s: str) -> bool:
    return len(s) == len(set(s))
            
def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        buffer = f.readline()
        i = 0
        while True:
            section = buffer[i:i + 14]
            if all_unique(section):
                return i + 14
            i += 1

    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
