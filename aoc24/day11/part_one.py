import sys


def blink(stones):
    new_stones = []
    for st in stones:
        if st == 0:
            new_stones.append(1)
        elif len(str(st)) % 2 == 0:
            middle = len(str(st)) // 2
            new_stones.append(int(str(st)[:middle]))
            new_stones.append(int(str(st)[middle:]))
        else:
            new_stones.append(st*2024)
    return new_stones


def main(stones):
    for i in range(25):
        stones = blink(stones)

    print(f'{stones}\n\nNumber of stones: {len(stones)}\n\n')

if __name__ == '__main__':
    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    stones = list(map(int, lines[0].split()))
    main(stones)