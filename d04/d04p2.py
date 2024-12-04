with open ("input.txt", "r") as file:
    grid = file.read().strip().split("\n")
sum = 0
strings = ["MMSS", "SSMM", "MSMS", "SMSM"]
for row in range(1, len(grid) - 1):
    for col in range(1, len(grid[0]) - 1):
        if grid[row][col] == "A":
            edges = [grid[row - 1][col - 1], grid[row - 1][col + 1], grid[row + 1][col - 1], grid[row + 1][col + 1]]
            join_edges = "".join(edges)
            if join_edges in strings:
                sum += 1
print(sum)