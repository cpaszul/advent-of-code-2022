from string import ascii_letters

DEFAULT_INPUT = 'day3.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    total = 0
    with open(loc) as f:
        for line in f.readlines():
            line = line.strip()
            first, second = set(line[:len(line)//2]), set(line.strip()[len(line)//2:])
            common = list(first & second)[0]
            total += ascii_letters.index(common) + 1
    return total
            
def part_2(loc: str = DEFAULT_INPUT) -> int:
    total = 0
    with open(loc) as f:
        for i, line in enumerate(f.readlines()):
            line = line.strip()
            if i % 3 == 0:
                first = set(line)
            if i % 3 == 1:
                second = set(line)
            if i % 3 == 2:
                third = set(line)
                common = list(first & second & third)[0]
                total += ascii_letters.index(common) + 1         
    return total

    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
