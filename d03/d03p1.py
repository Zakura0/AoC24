import re

def extract_mul_instructions(input):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, input)
    return matches

with open ("input.txt", "r") as file:
    input = file.read().strip()
    sum = 0
    for instruction in extract_mul_instructions(input):
        instruction = instruction.replace("mul(", "").replace(")", "").split(",")
        sum += int(instruction[0]) * int(instruction[1])
    print(sum)
