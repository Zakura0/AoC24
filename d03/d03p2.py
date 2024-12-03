import re

def extract_instructions(input):
    pattern = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, input)
    return matches

with open ("input.txt", "r") as file:
    input = file.read().strip()
    sum = 0
    enabled = True
    for instruction in extract_instructions(input):
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        if enabled and "mul" in instruction:
            instruction = instruction.replace("mul(", "").replace(")", "").split(",")
            sum += int(instruction[0]) * int(instruction[1])
    print(sum)
