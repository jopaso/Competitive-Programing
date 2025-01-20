import sys
def main(mapa, movements):
    pos_rob = (-1, -1)
    for i, line in enumerate(mapa):
        for j, c in enumerate(line):
            if c == '@':
                pos_rob = (i, j)

    for movement in movements:
        _, pos_rob = move(mapa, pos_rob, movement, '@')
        
    
    # for line in mapa:
    #     print(line)
    # print(f'\n\n')

    suma = 0
    for i, line in enumerate(mapa):
        for j, charac in enumerate(line):
            if charac == 'O':
                suma += (100*i) + j

    print(f'\nSUMA: {suma}')
def move(mapa, pos, direct, obj):
    next_pos = (-1, -1)
    match direct:
        case '^':
            next_pos = (pos[0] - 1,pos[1])
        case 'v':
            next_pos = (pos[0] + 1,pos[1])
        case '<':
            next_pos = (pos[0], pos[1] - 1)
        case '>':
            next_pos = (pos[0],pos[1] + 1)


    if mapa[next_pos[0]][next_pos[1]] == '#':
                return False, pos #Couldn't move
    elif mapa[next_pos[0]][next_pos[1]]== 'O':
        done, _ = move(mapa, next_pos, direct, 'O')
        if done:
            mapa[next_pos[0]][next_pos[1]] = obj
            mapa[pos[0]][pos[1]] = '.'
            return True, next_pos
        
        else:
            return False, pos #Couldn't move
    else: #Empty space
        mapa[next_pos[0]][next_pos[1]] = obj
        mapa[pos[0]][pos[1]] = '.'
        return True, next_pos



if __name__ == '__main__':
    lines = []
    movements = ""
    with open(sys.argv[1], 'r') as f:
        while True:
            a = f.readline().strip()
            if not a:
                break
            
            lines.append(a)
        
        while True:
            a = f.readline().strip()
            if not a:
                break
            movements += a

    mapa = []
    for l in lines:
        line = []
        for c in l:
            line.append(c)
        mapa.append(line)
    #print(f'Map: {map}\n\nMovements: {movements}')
    main(mapa, movements)