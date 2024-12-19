with open("input.txt", "r") as file:
    byte_positions = file.read().strip().splitlines()

byte_positions = [[int(item) for item in line.split(",")] for line in byte_positions]

height = 71
width = 71

grid = [["." for _ in range(width)] for _ in range(height)]

def has_path():
    start = (0, 0)
    end = (height - 1, width - 1)
    queue = [start]
    visited = set()
    while queue:
        current = queue.pop(0)
        if current == end:
            return True
        if current in visited:
            continue
        visited.add(current)
        x, y = current
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < height and 0 <= new_y < width and grid[new_x][new_y] != "#":
                queue.append((new_x, new_y))
    return False

for i in range(len(byte_positions)):
    y, x = byte_positions[i]
    grid[x][y] = "#"
    if not has_path():
        print(y, x)
        break

# for row in grid:
#     print("".join(row))



