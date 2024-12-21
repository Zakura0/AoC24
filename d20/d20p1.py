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

# normal = find_shortest(s, e, grid, False)
# all_steps = {}
# for _ in range(10000):
#     steps = find_shortest(s, e, grid, True)
#     steps = normal - steps
#     if steps < 100:
#         break
#     if steps + normal in all_steps:
#         all_steps[steps + normal] += 1
#     else:
#         all_steps[steps + normal] = 1

# sorted_steps = dict(sorted(all_steps.items(), key=lambda item: item[0], reverse=True))
#print(sorted_steps)
# result = 0
# for key in all_steps:
#     result += all_steps[key]
# print(result)



def regularPath():
    node = s
    steps = 0
    path = {s:0}
    while node != e:
          row, col = node
          for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
              new_row, new_col = row + x, col + y
              if (new_row, new_col) not in path:
                  if 0 <= new_row < height and 0 <= new_col < width:
                      if grid[new_row][new_col] == '.':
                          steps += 1
                          node = (new_row, new_col)
                          path[node] = steps
                          break
    return path, steps
                     

def searchCheat(node, path, regular_time, max_time, max_cheat_time):
    global total_steps
    found_cheats = 0
    start_time = path[node]
    queue = OrderedDict()
    visited = set()
    queue[node] = start_time
    while queue:
        node, time = queue.popitem(last=False)
        visited.add(node)
        if (time - start_time) > max_cheat_time:
            break
        if node in path:
            if regular_time - path[node] + time <= max_time:
                found_cheats += 1
                steps = regular_time - path[node] + time
                if steps in total_steps:
                    total_steps[steps] += 1
                else:
                    total_steps[steps] = 1
        row, col = node
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_row, new_col = row + x, col + y
            if (new_row, new_col) not in queue and (new_row, new_col) not in visited:
                if 0 <= new_row < height and 0 <= new_col < width:
                    queue[(new_row, new_col)] = time + 1
    
    return found_cheats


regular_path, regular_time = regularPath()
max_time = regular_time - 100
total_cheats = 0
total_steps = {}
for node in regular_path:
    total_cheats += searchCheat(node, regular_path, regular_time, max_time, 20)

sorted_steps2 = dict(sorted(total_steps.items(), key=lambda item: item[0], reverse=True))
# test = sorted_steps.keys() - sorted_steps2.keys()
# print(test)
#print(sorted_steps2)
print(total_cheats)