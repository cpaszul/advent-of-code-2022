from functools import cache

DEFAULT_INPUT = 'day21.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    global MONKEYS
    MONKEYS = {}
    with open(loc) as f:
       for line in f.readlines():
           lhs, rhs = line.strip().split(': ')
           if any(char in rhs for char in '*+-/'):
               monkey_1, op, monkey_2 = rhs.split(' ')
               if op == '+':
                   MONKEYS[lhs] = [monkey_1, lambda a, b: a + b, monkey_2]
               if op == '-':
                   MONKEYS[lhs] = [monkey_1, lambda a, b: a - b, monkey_2]
               if op == '*':
                   MONKEYS[lhs] = [monkey_1, lambda a, b: a * b, monkey_2]
               if op == '/':
                   MONKEYS[lhs] = [monkey_1, lambda a, b: a // b, monkey_2]
           else:
                MONKEYS[lhs] = int(rhs)
    return monkey_value('root')

@cache
def monkey_value(monkey: str) -> int:
    global MONKEYS
    val = MONKEYS[monkey]
    if isinstance(val, int):
        return val
    monkey_1, op, monkey_2 = val
    return op(monkey_value(monkey_1), monkey_value(monkey_2))
    
def part_2(loc: str = DEFAULT_INPUT) -> int:
    global MONKEYS
    MONKEYS = {}
    with open(loc) as f:
        for line in f.readlines():
            lhs, rhs = line.strip().split(': ')
            if lhs == 'root':
                monkey_1, op, monkey_2 = rhs.split(' ')
                MONKEYS[lhs] = [monkey_1, lambda a, b: a == b, monkey_2]
            elif any(char in rhs for char in '*+-/'):
                monkey_1, op, monkey_2 = rhs.split(' ')
                if op == '+':
                    MONKEYS[lhs] = [monkey_1, lambda a, b: a + b, monkey_2]
                if op == '-':
                    MONKEYS[lhs] = [monkey_1, lambda a, b: a - b, monkey_2]
                if op == '*':
                    MONKEYS[lhs] = [monkey_1, lambda a, b: a * b, monkey_2]
                if op == '/':
                    MONKEYS[lhs] = [monkey_1, lambda a, b: a // b, monkey_2]
            else:
                MONKEYS[lhs] = int(rhs)
    MONKEYS['humn'] = 0
    start_dir = monkey_value2('root')
    i = 0
    inc = 10000000000000000000000
    while True:
        monkey_value2.cache_clear()
        i += inc
        MONKEYS['humn'] = i
        val = monkey_value2('root')
        if val == '==':
            return i
        if val != start_dir:
            i -= inc
            inc //= 10

@cache
def monkey_value2(monkey: str) -> int | str:
    global MONKEYS
    val = MONKEYS[monkey]
    if isinstance(val, int):
        return val
    monkey_1, op, monkey_2 = val
    monkey_1 = monkey_value2(monkey_1)
    monkey_2 = monkey_value2(monkey_2)
    if monkey == 'root':
        if monkey_1 < monkey_2:
            return '<'
        elif monkey_1 > monkey_2:
            return '>'
        else:
            return '=='
    return op(monkey_1, monkey_2)

    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
