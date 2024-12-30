with open("input_swapped.txt", "r") as file:
    blocks = file.read().strip().split("\n\n")

wires = {}
statements = {}

for line in blocks[0].splitlines():
    split = line.split(": ")
    wire, state = split[0], split[1]
    wires[wire] = int(state)
    
for line in blocks[1].splitlines():
    wire1, gate, wire2, _, result = line.split()
    wires[result] = None
    statements[result] = (gate, wire1, wire2)

def evaluate(wire):
    if wires[wire] is not None and wire in wires:
        return wires[wire]
    gate, wire1, wire2 = statements[wire]
    val1 = evaluate(wire1)
    val2 = evaluate(wire2)
    if gate == "AND":
        result = val1 & val2
    elif gate == "OR":
        result = val1 | val2
    elif gate == "XOR":
        result = val1 ^ val2
    wires[wire] = result
    return result

def checkWire(check, expected):
    for wire in wires:
        if wire.startswith("x") or wire.startswith("y"):
            continue
        else:
            wires[wire] = None
    evaluate(check)
    if wires[check] != expected:
        return False
    else:
        return True

def print_tree(wire, indent=0, max_depth=2, current_depth=0):
    if current_depth > max_depth or wire not in statements:
        print(" " * indent + f"{wire}")
        return
    gate, wire1, wire2 = statements[wire]
    print(" " * indent + f"{wire}: {gate}")
    print_tree(wire1, indent + 4, max_depth, current_depth + 1)
    print_tree(wire2, indent + 4, max_depth, current_depth + 1)

def checkBit(index):
    for wire in wires:
        if wire.startswith("x") or wire.startswith("y"):
            wires[wire] = 0
    x = f"x{index:02}"
    y = f"y{index:02}"
    z = f"z{index:02}"

    failed = False

    wires[x] = 0
    wires[y] = 0
    if not checkWire(z, 0):
        failed = True
    wires[x] = 1
    wires[y] = 0
    if not checkWire(z, 1):
        failed = True
    wires[x] = 0
    wires[y] = 1
    if not checkWire(z, 1):
        failed = True
    wires[x] = 1
    wires[y] = 1
    if not checkWire(z, 0):
        failed = True
    
    if failed:
        print("Check failed at " + z)
        print_tree(z)
        return True
    return False
        
for i in range(45):
    if checkBit(i):
        break
else:
    print("Passed!")

swapped = ["vwr", "z06", "tqm", "z11", "z16", "kfs", "gfv", "hcm"]
swapped = sorted(swapped)
print(",".join(swapped))
