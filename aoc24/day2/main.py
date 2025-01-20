
def check_conditions(values):
    print(values)
    op = values[0] - values[1]

    if op > 0 and op <= 3 : #decreasing
        for i in range(len(values) - 1):
            op = values[i] - values[i+1]
            if not op > 0 or op > 3:
                return False
    elif op < 0 and op >= -3: #increasing
        for i in range(len(values) - 1):
            op = values[i] - values[i+1]
            if not op < 0 or op < -3:
                return False       
    else:
        return False
    
    return True

def main():
    safe = 0
    with open("input.in", 'r') as file:
        input = file.readlines()
        for line in input:
            values = list(map(lambda x: int(x), line.split(" ")))
            if check_conditions(values) or any (check_conditions(values[:i] + values[i+1:]) for i in range(len(values))):
                safe += 1
                print(f'report {values} is safe')
    
    print(f'Safe reports: {safe}')
    
    print("END")
    

if __name__ == "__main__":
    main()

