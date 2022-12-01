DEFAULT_INPUT = 'day1.txt'

def day_1(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    with open(loc) as f:
        elves = [sum(map(int, elf.split('\n'))) for elf in f.read().split('\n\n')]
    elves.sort(reverse=True)
    return elves[0], sum(elves[:3])

if __name__ == '__main__':
    part_1, part_2 = day_1()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
