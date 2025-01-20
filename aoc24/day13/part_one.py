import sys

def compute_movements(ma):
    x = ma['a']['x']
    z = ma['b']['x']
    r1 = ma['prize']['x']

    t = ma['a']['y']
    v = ma['b']['y']
    r2 = ma['prize']['y']

    a = ((v*r1) - (z*r2))/((v*x) - (t*z))
    b = (r2 - (a*t)) / v

    return a,b

def main(machines):
    total_tokens = 0
    for ma in machines:
        try: 
            a, b = compute_movements(ma)
            tokens = a*3 + b*1
            mod = tokens%1
            if mod == 0 and a <= 100 and b <= 100:
                total_tokens += tokens
                print(f'Movements button A: {a}\nMovements button B: {b}\nTotal tokens: {tokens}')
        except:
            pass

    print(f'\n\n Total tokens: {total_tokens}')
def formate(string):
    string = string.replace("Button ", "")
    but, place = string.split(": ")
    x, y = place.split(", ")
    if but == 'Prize':
        x = int(x.replace('X=', ""))
        y = int(y.replace('Y=', ""))
    else:
        x = int(x.replace('X+', ""))
        y = int(y.replace('Y+', ""))


    return {'x': x, 'y':y}

if __name__ == '__main__':
    lines = []
    with open(sys.argv[1], 'r') as f:
        while True:
            a = f.readline().strip()
            if not a:
                break
            a = formate(a)
            b = formate(f.readline().strip())
            prize = formate(f.readline().strip())
            f.readline() # empty line

            d = {'a': a, 'b': b, 'prize': prize}
            lines.append(d)

    for li in lines:
        print(li)

    main(lines)    
    
