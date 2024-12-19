with open("input.txt", "r") as file:
    byte_positions = file.read().strip().splitlines()

byte_positions = [[int(item) for item in line.split(",")] for line in byte_positions]

height = 71
width = 71

grid = [["." for _ in range(width)] for _ in range(height)]

def has_path(grid):
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

upper = len(byte_positions) - 1
lower = 0
while lower < upper:
    middle = (upper + lower) // 2
    grid_copy = [list(row) for row in grid]
    for i in range(middle + 1):
        y, x = byte_positions[i]
        grid_copy[x][y] = "#"
    if has_path(grid_copy):
        lower = middle + 1
    else:
        upper = middle
    
x, y = byte_positions[lower]
print(x,y)

# for row in grid_copy:
#     print("".join(row))





