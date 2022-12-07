DEFAULT_INPUT = 'day7.txt'

def day_7(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    global DIR_SIZES
    DIR_SIZES = []
    with open(loc) as f:
        lines = [line.strip() for line in f.readlines()]
    get_total_size(lines, 1)
    total_size = max(DIR_SIZES)
    free_size = 70000000 - total_size
    needed_size = 30000000 - free_size
    return sum(d for d in DIR_SIZES if d <= 100000), \
           min((d for d in DIR_SIZES if d >= needed_size))

def get_total_size(lines: list[str], i: int) -> tuple[int, int]:
    global DIR_SIZES
    size = 0
    while True:
        if i >= len(lines) or lines[i] == '$ cd ..':
            DIR_SIZES.append(size)
            return size, i + 1
        elif lines[i].startswith('$ cd'):
            dir_size, i = get_total_size(lines, i + 1)
            size += dir_size
        elif lines[i].startswith('$ ls') or lines[i].startswith('dir'):
            i += 1
        else:
            size += int(lines[i].split(' ')[0])
            i += 1

    
if __name__ == '__main__':
    part_1, part_2 = day_7()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)

