with open("input.txt", "r") as input:
    parts = input.read().strip().split("\n\n")
orders = parts[0].splitlines()
orders = [list(map(int, order.split("|"))) for order in orders]
instructions = {}
for x, y in orders:
    if x not in instructions:
        instructions[x] = [y]
    else:
        instructions[x].append(y)

updates = parts[1].splitlines()
updates = [list(map(int, update.split(","))) for update in updates]
middles = []
for update in updates:
    for i in range(len(update) - 1):
        if update[i] not in instructions:
            instructions[update[i]] = []
        if update[i + 1] in instructions[update[i]]:
            continue
        else:
            break
    else:
        middles.append(update[len(update) // 2])

print(sum(middles))

