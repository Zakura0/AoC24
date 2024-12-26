with open("input.txt", "r") as file:
    grids = file.read().strip().split("\n\n")

locks = set()
keys = set()

for grid in grids:
    lines = grid.splitlines()
    if lines[0].startswith("#"):
        lock = []
        for col in range(len(lines[0])):
            height = -1
            for row in range(len(lines)):
                if lines[row][col] == "#":
                    height += 1
                continue
            lock.append(height)
        lock = tuple(lock)
        locks.add(lock)
    else:
        key = []
        for col in range(len(lines[0])):
            height = 6
            for row in range(len(lines)):
                if lines[row][col] == ".":
                    height -= 1
                continue
            key.append(height)
        key = tuple(key)    
        keys.add(key)

result = 0

for lock in locks:
    for key in keys:
        for i in range(len(lock)):
            if lock[i] + key[i] > 5:
                break
        else:
            result +=  1

print(result)

            


