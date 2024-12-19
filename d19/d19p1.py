from functools import cache

with open("input.txt", "r") as file:
    blocks = file.read().strip().split("\n\n")

towels =  blocks[0].split(", ")
designs = blocks[1].splitlines()
towels = set(towels)

result = 0

@cache
def checkPossible(design):
    if design == "":
        return True
    possible = False
    for towel in towels:
        if towel in design:
            possible = True
            rest = design.split(towel)
            for part in rest:
                possible = checkPossible(part) and possible
            if possible:
                return True
    return False

for design in designs:
    if checkPossible(design):
        result += 1

print(result)