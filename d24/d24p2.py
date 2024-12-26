with open("input.txt", "r") as file:
    blocks = file.read().strip().split("\n\n")

wires = {}
statements = []

for line in blocks[0].splitlines():
    split = line.split(": ")
    wire, state = split[0], split[1]
    wires[wire] = int(state)

for line in blocks[1].splitlines():
    split = line.split(" -> ")
    result = split[1]
    wires[result] = None
    gate = ""
    if "XOR" in split[0]:
        split = split[0].split(" XOR ")
        wire1, wire2 = split[0], split[1]
        gate = "^"
    elif "OR" in split[0]:
        split = split[0].split(" OR ")
        wire1, wire2 = split[0], split[1]
        gate = "|"
    elif "AND" in split[0]:
        split = split[0].split(" AND ")
        wire1, wire2 = split[0], split[1]
        gate = "&"
    statements.append((wire1, wire2, result, gate))

done = set()

while any(value is None for value in wires.values()):
    for element in statements:
        wire1, wire2, result, gate = element
        if wires[wire1] is None or wires[wire2] is None:
                continue
        if gate == "^":
            wires[result] = wires[wire1] ^ wires[wire2]
        elif gate == "|":
            wires[result] = wires[wire1] or wires[wire2]
        else:
            wires[result] = wires[wire1] and wires[wire2]

wires = dict(sorted(wires.items()))
x = ""
y = ""
result = ""
for key in wires:
    if key.startswith("z"):
        result = str(wires[key]) + result
    if key.startswith("x"):
        x = str(wires[key]) + x
    if key.startswith("y"):
        y = str(wires[key]) + y

expected = int(x, 2) + int(y, 2)
expected = bin(expected)[2:]
#result = int(result, 2)

wrong = []
index = []

for i, char in enumerate(expected):
    if char != result[i]:
        key = sorted(wires)[-i]
        wrong.append(key)

affected = {}

for w in wrong:
    for s in statements:
        w1, w2, r, operator =  s
        if r == w:
            if w not in affected:
                affected[w] = [w1, w2]