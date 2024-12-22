with open("input.txt", "r") as file:
    blocks = file.read().strip().split("\n\n")

program = list(map(int, blocks[1].split(": ")[1].split(",")))
B = 0
C = 0
A = 0

def combo(operand):
    global A
    global B
    global C
    match operand:
        case 1 | 2 | 3 :
            return operand
        case 4:
            return A
        case 5:
            return B
        case 6:
            return C
        case 7:
            raise Exception("Combo Operand 7")
        
def processA(a):
    global A
    global B
    global C
    A = a
    B = 0
    C = 0
    i = 0
    output = []
    while i < len(program):
        instruction = program[i]
        operand = program[i + 1]    
        match instruction:
            case 0:
                A = A >> combo(operand)
            case 1:
                B = B ^ operand
            case 2:
                B = combo(operand) & 7
            case 3:
                if A != 0:
                    i = operand
                    continue
            case 4:
                B =  B ^ C
            case 5:
                res = combo(operand) & 7
                output.append(res)
            case 6:
                B = A >> combo(operand)
            case 7:
                C = A >> combo(operand)
        i += 2
    return output

valid = {0}
for num in program[::-1]:
    next_valid = set()
    for a in valid:
        for bits in [0b0000, 0b0001, 0b0010, 0b0011, 0b0100, 0b0101, 0b0110, 0b0111]:
            a_shifted = a << 3
            a_shifted += bits
            if processA(a_shifted)[0] == num:
                next_valid.add(a_shifted)
    valid = next_valid
print(min(valid))

    




