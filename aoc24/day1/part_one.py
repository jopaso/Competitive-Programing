

def main():
    with open('input.in', 'r') as file:
        lines = file.readlines()
        pairs = list(map(lambda x: x.strip().split(), lines))
        left = []
        right = []
        for i in pairs:
            left.append(i[0])
            right.append(i[1])
        
        left.sort()
        right.sort()
        distance = 0
        for l, r in zip(left, right):
            distance += abs(int(l) - int(r))
        
        print(f'The distance between the lists is: {distance}')


if __name__ == '__main__':
    main()