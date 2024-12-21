import sys

sys.setrecursionlimit(9400)

with open("sample.txt", "r") as file:
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
    timer = 20
    if not cheatAllowed:
        timer = 0
    first_cheat = (-1, -1)
    final_cheat = (-1, -1)
    final_final_cheat = (-1, -1)
    queue = [(start, 0, first_cheat, final_cheat, timer)]
    visited = set()
    while queue:
        current, steps, first_cheat, final_cheat, timer = queue.pop(0)
        if current == end:
            if (cheatAllowed):
                cheatedAt.add((first_cheat, final_cheat))
            return steps
        if (current, first_cheat, final_cheat) in visited:
            continue
        visited.add((current, first_cheat, final_cheat))
        x, y = current
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < height and 0 <= new_y < width:
                if grid[new_x][new_y] == "#" and timer > 0:
                    if timer == 20:
                        first_cheat = (x, y)
                        final_cheat = (new_x, new_y)
                        queue.append(((new_x, new_y), steps + 1, first_cheat, final_cheat, timer - 1))
                    else:
                        if (first_cheat, (new_x, new_y)) not in cheatedAt:
                            if final_cheat in [(new_x + 1, new_y + 0), (new_x + -1, new_y + 0), (new_x + 0, new_y + 1), (new_x + 0, new_y + -1)]:
                                final_cheat = (new_x, new_y)
                                queue.append(((new_x, new_y), steps + 1, first_cheat, final_cheat, timer - 1))                         
                elif grid[new_x][new_y] != "#":
                    queue.append(((new_x, new_y), steps + 1, first_cheat, final_cheat, timer))
    return -1

#normal = find_shortest(s, e, grid, False)
# best = find_shortest(s, e, grid, True)
# print(best)
all_steps = {}
for _ in range(1):
    steps = find_shortest(s, e, grid, True)
    #steps = normal - steps
    # if steps < 76:
    #     break
    if steps in all_steps:
        all_steps[steps] += 1
    else:
        all_steps[steps] = 1
print(cheatedAt)

sorted_steps = dict(sorted(all_steps.items(), key=lambda item: item[0], reverse=True))
print(sorted_steps)
# result = 0
# for key in sorted_steps:
#     if key >= 100:
#         result+= sorted_steps[key]
# print(result)