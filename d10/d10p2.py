with open("input.txt", "r") as file:
    grid = file.read().strip().splitlines()
grid = [[int(char) for char in line] for line in grid]

height = len(grid)
width = len(grid[0])

def checkTrailheads(grid, r, c):
    queue = []
    seen = {}
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue.append((r,c))
    while queue:
        cur = queue.pop(0)
        r, c = cur[0], cur[1]
        for d in directions:
            if r + d[0] >= 0 and r + d[0] < height and c + d[1] >= 0 and c + d[1] < width:
                if (r + d[0], c + d[1]) in seen:
                    seen[(r + d[0], c + d[1])] += 1
                elif grid[r + d[0]][c + d[1]] == grid[r][c] + 1:
                        if (grid[r + d[0]][c + d[1]] == 9):
                            seen[(r + d[0], c + d[1])] = 1
                        else:
                            queue.append((r + d[0], c + d[1]))
    sum = 0
    for key in seen:
        sum += seen[key]
    return sum
        
                    
result = 0
for r in range(height):
    for c in range(width):
        if grid[r][c] == 0:
            result += checkTrailheads(grid, r, c)
print(result)