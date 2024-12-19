with open("input.txt", "r") as file:
    byte_positions = file.read().strip().splitlines()

byte_positions = [[int(item) for item in line.split(",")] for line in byte_positions]

height = 71
width = 71

grid = [["." for _ in range(width)] for _ in range(height)]

for i in range(1024):
    y, x = byte_positions[i]
    grid[x][y] = "#"

# for row in grid:
#     print("".join(row))

def dijsktra():
    start = (0, 0)
    end = (height - 1, width - 1)
    queue = [(start, 0)]
    visited = set()
    while queue:
        current, steps = queue.pop(0)
        if current == end:
            return steps
        if current in visited:
            continue
        visited.add(current)
        x, y = current
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < height and 0 <= new_y < width and grid[new_x][new_y] != "#":
                queue.append(((new_x, new_y), steps + 1))
    return -1

print(dijsktra())


