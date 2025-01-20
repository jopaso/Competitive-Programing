

def form(line):
    arr = line.strip().split(': ')
    value = arr[0]
    numbers = list(map(lambda x: int(x), arr[1].split()))

    return int(value), numbers

def try_ops(value, numbers):
    return try_options(value, numbers[1::], numbers[0], '*') or try_options(value, numbers[1::], numbers[0], '+')

def try_options(value, numbers, act_val, op):
    if len(numbers) <= 0 :
        return act_val == value
    elif act_val > value and len(numbers) >= 1:
        return False

    if op == '*':
        act_val *= numbers[0]
    else:
        act_val += numbers[0]

    return try_options(value, numbers[1::], act_val, '*') or try_options(value, numbers[1::], act_val, '+')

def main():
    lines = []
    with open('input.in', 'r') as fi:
        lines = fi.readlines()
    
    result = 0
    for line in lines:
        value, numbers = form(line)
        
        if (try_ops(value, numbers)):
            result += value
            print(f'Value: {value}, numbers: {numbers[0]} TRUE')


    print(f'Final result: {result}')



if __name__ == '__main__':
    main()