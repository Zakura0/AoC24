import heapq

with open("input.txt", "r") as file:
    grid = file.read().strip().splitlines()

height = len(grid)
width = len(grid[0])

end = (0, 0)

for r in range(height):
    for c in range(width):
        if grid[r][c] == "S":
            sr, sc = r, c
        elif grid[r][c] == "E":
            end = (r, c)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d = 0
start = (sr, sc, d)

def options(pos, grid):
    pr, pc, pd = pos
    yield (1000, (pr, pc, (pd - 1) % 4)) #gegen uhrzeigersinn drehen
    yield (1000, (pr, pc, (pd + 1) % 4)) #im uhrzeigersinn drehen
    dr, dc = directions[pd]
    if grid[pr + dr][pc + dc] != "#":
        yield (1, (pr + dr, pc + dc, pd))

def dijkstra(grid, start, end):
    queue = [(0, start)]
    seen = set()
    seen.add(start)
    while queue:
        total_cost, pos = heapq.heappop(queue)
        seen.add(pos)
        cr, cc, _ = pos
        if (cr, cc) == end:
            return total_cost
        for cost, option in options(pos, grid):
            if option in seen:
                continue
            heapq.heappush(queue, (total_cost + cost, option))

print(dijkstra(grid, start, end))
    