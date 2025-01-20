

def main():
    with open('input.in', 'r') as file:
        lines = file.readlines()
        pairs = list(map(lambda x: x.strip().split(), lines))
        left = []
        right = []
        for i in pairs:
            left.append(i[0])
            right.append(i[1])
        
        
        similarity = 0
        for l in left:
            similarity += int(l) * right.count(l)
        
        print(f'The similarity between the lists is: {similarity}')


if __name__ == '__main__':
    main()