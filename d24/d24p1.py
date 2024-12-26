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

result = ""
wires = dict(sorted(wires.items()))
for key in wires:
    if key.startswith("z"):
        result = str(wires[key]) + result

print(int(result, 2))
