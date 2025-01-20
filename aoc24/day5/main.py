

def form(line):
    
    line = list(map(lambda x: int(x), line.strip().split(',')))
    return line

def check_sim(tupla, comb):
    return tupla in comb

def check_conditions(line, before, comb):
    if any (check_sim((line[after], line[before]), comb) for after in range(before+1, len(line))):
        #print('Line incorrect')
        return True
    #print('Line correct')
    return False

def correct(line, comb):
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            if check_sim((line[j], line[i]), comb):
                line[i], line[j] = line[j], line[i]
                return correct(line, comb)
    return line

def main():
    lines = []
    with open('input.in', 'r') as f:
        lines = f.readlines()
    
    comb = []
    dictLine = 0
    for i, line in enumerate(lines):
        line.strip()
        if len(line) <= 1:
            dictLine = i+1
            break
        arr=line.strip().split('|')
        comb.append((int(arr[0]), int(arr[1])))

    lines=lines[dictLine::]
    lines = list(map(form, lines))

    suma=0
    for line in lines:
     #   print(f'Checking line: {line}')
        if (any(check_conditions(line, i, comb) for i in range(len(line)))):
            print(f'INCORRECT')
            line = correct(line, comb)
            suma += line[len(line)//2]
        else:
            print(f'Line correct')
            #suma += line[len(line)//2]
        
    print(f'Suma = {suma}')




if __name__ == '__main__':
    main()