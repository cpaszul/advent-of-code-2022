import re

DEFAULT_INPUT = 'day4.txt'

def day_4(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    p = re.compile(r'(\d+)-(\d+),(\d+)-(\d+)')
    part_1_res = 0
    part_2_res = 0
    with open(loc) as f:
        for line in f.readlines():
            m = p.match(line)
            start_a, end_a, start_b, end_b = map(int, (m.group(1), m.group(2),
                                                       m.group(3), m.group(4)))
            if (start_a >= start_b and end_a <= end_b) or \
               (start_b >= start_a and end_b <= end_a):
                part_1_res += 1
            if (start_a <= start_b <= end_a) or (start_a <= end_b <= end_a) or \
               (start_b <= start_a <= end_b) or (start_b <= end_a <= end_b):
                part_2_res += 1
    return part_1_res, part_2_res

    
if __name__ == '__main__':
    part_1, part_2 = day_4()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
