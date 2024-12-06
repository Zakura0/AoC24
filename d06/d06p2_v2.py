import copy
import time
start_time = time.time()
with open("input.txt", "r") as file:
    grid = file.read().strip().split("\n")

height = len(grid)
width = len(grid[0])

def is_loop(grid, sr, sc, getPath):
    dir_num = 3
    seen = set()
    c_row, c_col = sr, sc
    while True:
        dir = direction_loop[dir_num]
        if (c_row, c_col, dir) in seen:
            return True
        seen.add((c_row, c_col, dir))
        n_row, n_col = c_row + dir[0], c_col + dir[1]
        if n_row < 0 or n_row >= height or n_col < 0 or n_col >= width:
            if getPath:
                return seen
            return False
        elif grid[n_row][n_col] == "#":
                dir_num = (dir_num + 1) % 4
        else:
            c_row, c_col = n_row, n_col

for row in range(width):
    for col in range(height):
        if grid[row][col] == "^":
            s_row, s_col = row, col
direction_loop = [(0, 1), (1, 0), (0, -1), (-1, 0)]
loops = 0
path = is_loop(grid, s_row, s_col, True)
path = {(r, c) for r, c, d in path}
for (r, c) in path:
    if (r, c) == (s_row, s_col):
        continue
    grid_copy = copy.deepcopy(grid)
    grid_copy[r] = grid_copy[r][:c] + "#" + grid_copy[r][c+1:]
    if is_loop(grid_copy, s_row, s_col, False):
        loops += 1
end_time = time.time()
runtime = end_time - start_time
print(f"Runtime: {runtime:.6f} seconds")
print(loops)











