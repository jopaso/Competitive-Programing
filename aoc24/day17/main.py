import sys


def main(register, program):

    print(f'\n')
    output = ""
    i = 0
    while i < len(program):
        
        opcode, operand = program[i], program[i+1]
        combo_operand = operand

        if operand == 4:
            combo_operand = register["A"]
        elif operand == 5:
            combo_operand = register["B"]
        elif operand == 6:
            combo_operand = register["C"]
        
        match opcode:
            case 0: #adv
                register["A"] = division(register["A"], combo_operand)
            
            case 1: #bxl
                register["B"] = xor(register["B"], operand)
                
            case 2: #bst
                register["B"] = modulo(combo_operand)
            case 3: #jnz
                if not register['A'] == 0:
                    i = operand - 2
                    print(f'Volviendo a  {operand}, i = {i}')
            case 4: #bxc
                register['B'] = xor(register['B'], register['C'])
            case 5: #out
                output += f',{modulo(combo_operand)}'
                print(f'printing: {modulo(combo_operand)}')
            case 6: #bdv
                register["B"] = division(register["A"], combo_operand) 
            case 7: #cdv
                register["C"] = division(register["A"], combo_operand)

        i += 2
    print(f'\n{output[1:]}\n')
    

def division(numerator, denominator):
    return numerator // (2**denominator)

def xor(num1, num2):
    return num1 ^ num2

def modulo(num1):
    return num1 % 8

if __name__ == '__main__':
    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines();

    registers = {'A' : int(lines[0].strip().split()[-1]),
              'B' : int(lines[1].strip().split()[-1]),
              'C' : int(lines[2].strip().split()[-1]),}

    
    pl = lines[-1].strip().split()[-1].split(",")
    program = list(map(int, pl))

    print(registers)
    print(program)

    main(registers, program)