import copy
import time
start_time = time.time()
with open("input.txt", "r") as file:
    grid = file.read().strip().split("\n")

height = len(grid)
width = len(grid[0])

c_row, c_col = 0, 0
for row in range(width):
    for col in range(height):
        if grid[row][col] == "^":
            s_row, s_col = row, col
direction_loop = [(0, 1), (1, 0), (0, -1), (-1, 0)]

loops = 0
for i in range(height):
    for j in range(width):
        c_row, c_col = s_row, s_col
        dir_num = 3
        seen = {}
        grid_copy = copy.deepcopy(grid)
        if grid_copy[i][j] == "#" or grid_copy[i][j] == "^":
            continue
        grid_copy[i] = grid_copy[i][:j] + "#" + grid_copy[i][j+1:] # wow all das um einen char zu tauschen
        while True:
            if (c_row, c_col) not in seen:
                seen[(c_row, c_col)] = 1
            else: seen[(c_row, c_col)] += 1
            if seen[(c_row, c_col)] > 4: #kann maximal 4 mal die gleiche position crossen, danach loop
                    loops += 1
                    break
            dir = direction_loop[dir_num]
            n_row, n_col = c_row + dir[0], c_col + dir[1]
            if n_row < 0 or n_row >= height or n_col < 0 or n_col >= width:
                break
            elif grid_copy[n_row][n_col] == "#":
                    dir_num = (dir_num + 1) % 4
            else:
                c_row, c_col = n_row, n_col
        continue
    print(i) #Programm ist bei 129 fertig x)
end_time = time.time()
runtime = end_time - start_time
print(f"Runtime: {runtime:.6f} seconds")
print(loops)





