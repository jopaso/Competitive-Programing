import sys
from collections import defaultdict


def blink(stones):
    new_stones = defaultdict(int)
    for st in stones:
        if st == 0:
            new_stones[1] += stones[st]
        elif len(str(st)) % 2 == 0:
            middle = len(str(st)) // 2
            new_stones[int(str(st)[:middle])] += stones[st]
            new_stones[int(str(st)[middle:])] += stones[st]
        else:
            new_stones[st*2024] += stones[st]
    return new_stones


def main(stones):
    for i in range(75):
        stones = blink(stones)

    sum = 0
    for num in stones:
        sum += stones[num]
    
    print(f'\n\nSTONES: {sum}')
    

if __name__ == '__main__':
    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    stones = list(map(int, lines[0].split()))
    nums = defaultdict(int)
    for st in stones:
        nums[st] += 1
    main(nums)