with open("input.txt", "r") as file:
    blocks = file.read().strip().split("\n\n")

A = 28066687
B = 0
C = 0

program = list(map(int, blocks[1].split(": ")[1].split(",")))

def combo(operand):
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

i = 0
output = ""
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
            output += f"{combo(operand) & 7},"
        case 6:
            B = A >> combo(operand)
        case 7:
            C = A >> combo(operand)
    i += 2
print(output[:-1])

