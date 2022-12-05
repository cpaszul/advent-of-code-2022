import re

DEFAULT_INPUT = 'day5.txt'

def part_1(loc: str = DEFAULT_INPUT) -> str:
    stacks = [None, [], [], [], [], [], [], [], [], []]
    p = re.compile('move (\d+) from (\d) to (\d)')
    with open(loc) as f:
        for line in f.readlines():
            if line[0] == '[':
                if line[1] != ' ':
                    stacks[1].append(line[1])
                if line[5] != ' ':
                    stacks[2].append(line[5])
                if line[9] != ' ':
                    stacks[3].append(line[9])
                if line[13] != ' ':
                    stacks[4].append(line[13])
                if line[17] != ' ':
                    stacks[5].append(line[17])
                if line[21] != ' ':
                    stacks[6].append(line[21])
                if line[25] != ' ':
                    stacks[7].append(line[25])
                if line[29] != ' ':
                    stacks[8].append(line[29])
                if line[33] != ' ':
                    stacks[9].append(line[33])
            if line != '\n' and line[1] == '1':
                for stack in stacks[1:]:
                    stack.reverse()
            if m := p.match(line):
                amount, start, end = map(int, (m.group(1), m.group(2), m.group(3)))
                for _ in range(amount):
                    char = stacks[start].pop()
                    stacks[end].append(char)
    return ''.join(stack[-1] for stack in stacks[1:])
            
def part_2(loc: str = DEFAULT_INPUT) -> str:
    stacks = [None, [], [], [], [], [], [], [], [], []]
    p = re.compile('move (\d+) from (\d) to (\d)')
    with open(loc) as f:
        for line in f.readlines():
            if line[0] == '[':
                if line[1] != ' ':
                    stacks[1].append(line[1])
                if line[5] != ' ':
                    stacks[2].append(line[5])
                if line[9] != ' ':
                    stacks[3].append(line[9])
                if line[13] != ' ':
                    stacks[4].append(line[13])
                if line[17] != ' ':
                    stacks[5].append(line[17])
                if line[21] != ' ':
                    stacks[6].append(line[21])
                if line[25] != ' ':
                    stacks[7].append(line[25])
                if line[29] != ' ':
                    stacks[8].append(line[29])
                if line[33] != ' ':
                    stacks[9].append(line[33])
            if line != '\n' and line[1] == '1':
                for stack in stacks[1:]:
                    stack.reverse()
            if m := p.match(line):
                amount, start, end = map(int, (m.group(1), m.group(2), m.group(3)))
                stacks[start], to_move = stacks[start][:-1 * amount], stacks[start][-1 * amount:]
                stacks[end].extend(to_move)
    return ''.join(stack[-1] for stack in stacks[1:])

    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
