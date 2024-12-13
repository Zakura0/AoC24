with open("input.txt", "r") as file:
    grid = file.read().strip().splitlines()

grid = [list(char for char in line) for line in grid]

height = len(grid)
width = len(grid[0])

regions = []
seen = set()

def findRegion(r, c):
    region = []
    queue = []
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue.append((r, c))
    plant = grid[r][c]
    while queue:
        cur = queue.pop(0)
        seen.add((cur[0], cur[1]))
        edges = 0
        r, c = cur[0], cur[1]
        for d in directions:
            if r + d[0] < 0 or r + d[0] >= height or c + d[1] < 0 or c + d[1] >= width:
                edges += 1
            elif grid[r + d[0]][c + d[1]] != plant:
                edges += 1
            else:
                if ((r + d[0], c + d[1])) not in seen:
                    queue.append((r + d[0], c + d[1]))
                    seen.add((r + d[0], c + d[1]))
        region.append((r, c, edges))
    return region

for r in range(height):
    for c in range(width):
        if ((r, c)) not in seen:
            regions.append(findRegion(r, c))

result = 0
for region in regions:
    edges = 0
    for plant in region:
        edges += plant[2]
    result += len(region) * edges

print(result)



                    


