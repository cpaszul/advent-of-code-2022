from math import prod

DEFAULT_INPUT = 'day11.txt'

class Monkey:
    def __init__(self, monkey_str: str) -> None:
        monkey_lines = monkey_str.split('\n')
        self.num = int(monkey_lines[0].split(' ')[1][0])
        self.items = list(map(int, monkey_lines[1].split(': ')[1].split(', ')))
        op, value = monkey_lines[2].split('= old ')[1].split(' ')
        if value == 'old':
            self.func = lambda x: x ** 2
        elif op == '+':
            self.func = lambda x: x + int(value)
        else:
            self.func = lambda x: x * int(value)
        self.test = int(monkey_lines[3].split(' ')[-1])
        self.true = int(monkey_lines[4].split(' ')[-1])
        self.false = int(monkey_lines[5].split(' ')[-1])

    def __repr__(self) -> str:
        return f'Monkey {self.num}, carrying {self.items} with function {self.func} \
and test {self.test}, passing to {self.true} and {self.false}'

    def inspect_p1(self) -> list[tuple[int, int]]:
        thrown_items = []
        for item in self.items:
            item = self.func(item)
            item //= 3
            if item % self.test == 0:
                thrown_items.append((item, self.true))
            else:
                thrown_items.append((item, self.false))
        self.items = []
        return thrown_items

    def inspect_p2(self, combined_test: int) -> list[tuple[int, int]]:
        thrown_items = []
        for item in self.items:
            item = self.func(item)
            item %= combined_test
            if item % self.test == 0:
                thrown_items.append((item, self.true))
            else:
                thrown_items.append((item, self.false))
        self.items = []
        return thrown_items

    def add_item(self, item: int) -> None:
        self.items.append(item)

def part_1(loc: str = DEFAULT_INPUT) -> str:
    with open(loc) as f:
        monkeys = [Monkey(m) for m in f.read().split('\n\n')]
    items_inspected = [0] * len(monkeys)
    for _ in range(20):
        for monkey in monkeys:
            items_inspected[monkey.num] += len(monkey.items)
            thrown_items = monkey.inspect_p1()
            for item_value, destination in thrown_items:
                monkeys[destination].add_item(item_value)
    items_inspected.sort(reverse = True)
    return items_inspected[0] * items_inspected[1]
            
def part_2(loc: str = DEFAULT_INPUT) -> str:
    with open(loc) as f:
        monkeys = [Monkey(m) for m in f.read().split('\n\n')]
    items_inspected = [0] * len(monkeys)
    combined_test = prod(monkey.test for monkey in monkeys)
    for _ in range(10000):
        for monkey in monkeys:
            items_inspected[monkey.num] += len(monkey.items)
            thrown_items = monkey.inspect_p2(combined_test)
            for item_value, destination in thrown_items:
                monkeys[destination].add_item(item_value)
    items_inspected.sort(reverse = True)
    return items_inspected[0] * items_inspected[1]

    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
