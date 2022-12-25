DEFAULT_INPUT = 'day25.txt'

def part_1(loc: str = DEFAULT_INPUT) -> str:
    with open(loc) as f:
        decimal_sum = sum(convert_to_decimal(line.rstrip()) for line in f.readlines())
    return convert_to_snafu(decimal_sum)

def convert_to_decimal(num: str) -> int:
    result = 0
    num = num[::-1]
    for i, ch in enumerate(num):
        place = 5 ** i
        if ch == '=':
            result -= 2 * place
        elif ch == '-':
            result -= place
        else:
            result += int(ch) * place
    return result

def convert_to_snafu(num: int) -> str:
    result = ''
    while num:
        if num % 5 == 0:
            result += '0'
        elif num % 5 == 1:
            result += '1'
            num -= 1
        elif num % 5 == 2:
            result += '2'
            num -= 2
        elif num % 5 == 3:
            result += '='
            num += 2
        else:
            result += '-'
            num += 1
        num //= 5
    return result[::-1]

    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
