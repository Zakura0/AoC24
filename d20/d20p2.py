with open("input.txt", "r") as file:
    grid = file.read().strip().splitlines()

grid = [list(char for char in line) for line in grid]

height = len(grid)
width = len(grid[0])

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

distance_to_start = {}

def find_path(s, e, grid):
    start = s
    end = e
    queue = [(start, 0)]
    visited = set()
    distance_to_start[start] = 0
    while queue:
        current, steps = queue.pop(0)
        if current in visited:
            continue
        visited.add(current)
        if current == end:
            return steps, visited
        x, y = current
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < height and 0 <= new_y < width:
                if grid[new_x][new_y] != "#":
                    next_pos = (new_x, new_y)
                    if next_pos not in visited:
                        queue.append((next_pos, steps + 1))
                        distance_to_start[next_pos] = steps + 1
    return -1

steps, path = find_path(s, e, grid)
cheat_seconds = 20 #set to 2 for p1
checked = set()
result = 0
for pos in path:
    for pos2 in path:
        if pos == pos2:
            continue
        if pos2 in checked or pos2 not in path:
            continue
        distance = abs(distance_to_start[pos] - distance_to_start[pos2])
        manhattan_distance = abs(pos[0] - pos2[0]) + abs(pos[1] - pos2[1])
        if manhattan_distance <= cheat_seconds and distance - manhattan_distance >= 100:
            result += 1
    checked.add(pos)
print(result) #takes around 20 seconds
                    



