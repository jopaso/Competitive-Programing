import sys
def main(mapa, movements):
    pos_rob = (-1, -1)
    for i, line in enumerate(mapa):
        for j, c in enumerate(line):
            if c == '@':
                pos_rob = (i, j)

    for movement in movements:
        # print(f'Move {movement}:')
        _, pos_rob = move(mapa, pos_rob, movement, '@')
        
    
    for line in mapa:
        print(line)
    print(f'\n\n')

    suma = 0
    for i, line in enumerate(mapa):
        for j, charac in enumerate(line):
            if charac == '[':
                suma += (100*i) + j

    print(f'\nSUMA: {suma}')

def check_box(mapa, left_pos, direct):
    next_pos = (-1, -1)
    match direct:
        case '^':
            next_pos = (left_pos[0] - 1,left_pos[1])
        case 'v':
            next_pos = (left_pos[0] + 1,left_pos[1])

    can_left = False
    can_right = False

    if mapa[next_pos[0]][next_pos[1]] == '#' or mapa[next_pos[0]][next_pos[1] + 1] == '#':
        return False
    
    if mapa[next_pos[0]][next_pos[1]] == '.':
        can_left = True
    elif mapa[next_pos[0]][next_pos[1]] == '[':
        return check_box(mapa, next_pos, direct)
    else:
        can_left = check_box(mapa, (next_pos[0], next_pos[1]-1), direct)

    if mapa[next_pos[0]][next_pos[1] + 1] == '.':
        can_right = True
    else: ## == '['
        can_right = check_box(mapa, (next_pos[0], next_pos[1]+1), direct)

    # print(f'Check box for {left_pos} --> {can_right and can_left}')

    return can_right and can_left
    
    
def move_box(mapa, left_pos, direct):
    next_pos = (-1, -1)
    match direct:
        case '^':
            next_pos = (left_pos[0] - 1,left_pos[1])
        case 'v':
            next_pos = (left_pos[0] + 1,left_pos[1])

    # print(f'Moving pos:{left_pos}')    
    if mapa[next_pos[0]][next_pos[1]] == '[':
        move_box(mapa, next_pos, direct)
    elif mapa[next_pos[0]][next_pos[1]] == ']':
        move_box(mapa, (next_pos[0], next_pos[1]-1), direct)


    if mapa[next_pos[0]][next_pos[1]+1] == '[':
        move_box(mapa, (next_pos[0], next_pos[1]+1), direct)


    mapa[next_pos[0]][next_pos[1]] = '['
    mapa[left_pos[0]][left_pos[1]] = '.'
    mapa[next_pos[0]][next_pos[1]+1] = ']'
    mapa[left_pos[0]][left_pos[1]+1] = '.'
    # for line in mapa:
    #     print(line)
    # print(f'\n\n')
    
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

    # for line in mapa:
    #     print(line)
    # print(f'\n\n')

    if mapa[next_pos[0]][next_pos[1]] == '#':
                return False, pos #Couldn't move
    elif mapa[next_pos[0]][next_pos[1]]== '[':
        if direct == '^' or direct == 'v':
            can_move = check_box(mapa, next_pos, direct)
            if can_move:
                move_box(mapa, next_pos, direct)
                mapa[next_pos[0]][next_pos[1]] = obj
                mapa[pos[0]][pos[1]] = '.'
                return True, next_pos
            else:
                return False, pos

        else:
            done1, _ = move(mapa, (next_pos[0] + 1, next_pos[1]), direct, ']')
            done2, _ = move(mapa, next_pos, direct, '[')
            if done1 and done2:
                mapa[next_pos[0]][next_pos[1]] = obj
                mapa[pos[0]][pos[1]] = '.'
                return True, next_pos
            
            else:
                return False, pos #Couldn't move

    elif mapa[next_pos[0]][next_pos[1]]== ']':
        if direct == '^' or direct == 'v':
            can_move = check_box(mapa, (next_pos[0], next_pos[1]-1), direct)
            if can_move:
                move_box(mapa, (next_pos[0], next_pos[1]-1), direct)
                mapa[next_pos[0]][next_pos[1]] = obj
                mapa[pos[0]][pos[1]] = '.'
                return True, next_pos
            else:
                return False, pos
        else:
            done1, _ = move(mapa, (next_pos[0], next_pos[1]-1), direct, '[')
            done2, _ = move(mapa, next_pos, direct, ']')
            if done1 and done2:
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
            if c == 'O':
                line += ['[', ']']
            elif c == '#':
                line += ['#', '#']
            elif c == '.':
                line += ['.', '.']
            else:
                line += ['@', '.']
        mapa.append(line)

    # for line in mapa:
    #     print(line)
    # print(f'\n\n')
    #print(f'Map: {map}\n\nMovements: {movements}')
    main(mapa, movements)