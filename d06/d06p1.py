with open("input.txt", "r") as file:
    grid = file.read().strip().split("\n")

height = len(grid)
width = len(grid[0])

c_row, c_col = 0, 0
for row in range(height):
    for col in range(width):
        if grid[row][col] == "^":
            c_row, c_col = row, col
direction_loop = [(0, 1), (1, 0), (0, -1), (-1, 0)]
seen = set()
seen.add((c_row, c_col))
dir_num = 3
while True:
    seen.add((c_row, c_col))
    dir = direction_loop[dir_num]
    n_row, n_col = c_row + dir[0], c_col + dir[1]
    if n_row < 0 or n_row >= height or n_col < 0 or n_col >= width:
        break
    elif grid[n_row][n_col] == "#":
        dir_num = (dir_num + 1) % 4
    else: 
        c_row, c_col = n_row, n_col
print(len(seen))





