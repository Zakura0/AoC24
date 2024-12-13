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
        sides = set()
        r, c = cur[0], cur[1]
        for d in directions:
            if r + d[0] < 0 or r + d[0] >= height or c + d[1] < 0 or c + d[1] >= width:
                continue
            else:
                if grid[r + d[0]][c + d[1]] == plant and ((r + d[0], c + d[1])) not in seen:
                    queue.append((r + d[0], c + d[1]))
                    seen.add((r + d[0], c + d[1]))
        region.append((r, c))
    return region

def countSides(region):
    edges = set()
    for r, c in region:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for d in directions:
            nr, nc = r + d[0], c + d[1]
            if (nr, nc) not in region:
                if r + d[0] == r:
                    edge = ("|", r, c, c + d[1])
                else:
                    edge = ("-", c, r, r + d[0])
                edges.add(edge)
    seen = set()
    sides = []
    for edge in edges:
        if edge in seen:
            continue
        seen.add(edge)
        coherent_edges = [edge]
        for direction in [1, -1]:
            i = 1
            while True:
                next_edge = (edge[0], edge[1] + i * direction, edge[2], edge[3])
                if next_edge in edges:
                    coherent_edges.append(next_edge)
                    seen.add(next_edge)
                    i += 1
                else:
                    break
        sides.append(coherent_edges)
    return len(sides)
            
for r in range(height):
    for c in range(width):
        if ((r, c)) not in seen:
            regions.append(findRegion(r, c))

result = 0
for region in regions:
    sides = countSides(region)
    result += sides * len(region)
print(result)
 


                    


