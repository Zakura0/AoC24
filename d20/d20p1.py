import sys
from collections import OrderedDict

sys.setrecursionlimit(9400)

with open("input.txt", "r") as file:
    grid = file.read().strip().splitlines()

grid = [list(char for char in line) for line in grid]

height = len(grid)
width = len(grid[0])
max_steps = 100

s = (0, 0)
e = (0, 0)

for r in range(height):
    for c in range(width):
        if grid[r][c] == "S":
            grid[r][c] = "."
            s = (r, c)
        elif grid[r][c] == "E":
            grid[r][c] = "."
            e = (r, c)

cheatedAt = set()

def find_shortest(s, e, grid, cheatAllowed):
    global cheatedAt
    start = s
    end = e
    cheat_pos = (-1, -1)
    cheated = True
    if cheatAllowed:
        cheated = False
    queue = [(start, 0, cheated, cheat_pos)]
    visited = set()
    while queue:
        current, steps, cheated, cheat_pos = queue.pop(0)
        if current == end:
            cheatedAt.add(cheat_pos)
            return steps
        if (current, cheated) in visited:
            continue
        visited.add((current, cheated))
        x, y = current
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < height and 0 <= new_y < width:
                if grid[new_x][new_y] == "#" and (new_x, new_y) not in cheatedAt:
                        if not cheated:
                            cheat_pos = (new_x, new_y)
                            queue.append(((new_x, new_y), steps + 1, True, cheat_pos))                     
                elif grid[new_x][new_y] != "#":
                    queue.append(((new_x, new_y), steps + 1, cheated, cheat_pos))
    return -1

normal = find_shortest(s, e, grid, False)
all_steps = {}
for _ in range(10000):
    steps = find_shortest(s, e, grid, True)
    steps = normal - steps
    if steps < 100:
        break
    if steps + normal in all_steps:
        all_steps[steps + normal] += 1
    else:
        all_steps[steps + normal] = 1

sorted_steps = dict(sorted(all_steps.items(), key=lambda item: item[0], reverse=True))
result = 0
for key in all_steps:
    result += all_steps[key]
print(result) #takes like 1 min



