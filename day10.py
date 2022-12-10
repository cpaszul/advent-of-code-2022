DEFAULT_INPUT = 'day10.txt'

def day_10(loc: str = DEFAULT_INPUT) -> tuple[int, list[list[str]]]:
    with open(loc) as f:
        instructs = [line.strip() for line in f.readlines()]
    reg = 1
    cycle = 1
    i = 0
    add_next = False
    value_to_add = 0
    signal_strength = 0
    pixels = []
    while True:
        if cycle in [20, 60, 100, 140, 180, 220]:
            signal_strength += cycle * reg
        pixel_x = (cycle - 1) % 40
        if (reg - 1) <= pixel_x <= (reg + 1):
            pixels.append('#')
        else:
            pixels.append(' ')
        cycle += 1
        if add_next:
            reg += value_to_add
            add_next = False
            i += 1
        else:
            try:
                inst = instructs[i]
            except IndexError:
                break
            if inst == 'noop':
                i += 1
            else:
                add_next = True
                value_to_add = int(inst.split(' ')[1])
    pixels = pixels[:240]
    pixels = list(zip(*[iter(pixels)]*40, strict=True))
    return signal_strength, pixels

    
if __name__ == '__main__':
    part_1, part_2 = day_10()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:')
    print('\n'.join(''.join(row) for row in part_2))
