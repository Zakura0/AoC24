with open ("input.txt", "r") as file:
    grid = file.read().strip().split("\n")
sum = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == "X":
            for d_row, d_col in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                if 0 <= row + 3 * d_row < len(grid) and 0 <= col + 3 * d_col < len(grid[0]):
                    if grid[row + d_row][col + d_col] == "M" and grid[row + 2 * d_row][col + 2 * d_col] == "A" and grid[row + 3 * d_row][col + 3 * d_col] == "S":
                        sum += 1
print(sum)


