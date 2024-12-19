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
        return 1
    count = 0
    for i in range(len(design) + 1):
        if design[:i] in towels:
            count += checkPossible(design[i:])
    return count

ans = 0
for design in designs:
    ans += checkPossible(design)
print(ans)