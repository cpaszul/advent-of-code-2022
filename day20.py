from collections import deque, namedtuple

DEFAULT_INPUT = 'day20.txt'

Number = namedtuple('Number', ['num_id', 'num'])

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        nums_fixed = [Number(i, int(line)) for i, line in enumerate(f.readlines())]
    nums = deque(nums_fixed)
    for n in nums_fixed:
        if n.num == 0:
            zero = n
        i = nums.index(n)
        nums.rotate(-1 * i)
        nums.popleft()
        nums.rotate(-1 * n.num)
        nums.appendleft(n)
    i = nums.index(zero)
    return nums[(i + 1000) % len(nums)].num + nums[(i + 2000) % len(nums)].num + \
           nums[(i + 3000) % len(nums)].num
        
def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        nums_fixed = [Number(i, int(line) * 811589153) for i, line in enumerate(f.readlines())]
    nums = deque(nums_fixed)
    for _ in range(10):
        for n in nums_fixed:
            if n.num == 0:
                zero = n
            i = nums.index(n)
            nums.rotate(-1 * i)
            nums.popleft()
            nums.rotate(-1 * n.num)
            nums.appendleft(n)
    i = nums.index(zero)
    return nums[(i + 1000) % len(nums)].num + nums[(i + 2000) % len(nums)].num + \
           nums[(i + 3000) % len(nums)].num

    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
