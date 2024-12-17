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

def options(total, pos, grid):
    pr, pc, pd = pos
    yield (1000 + total , (pr, pc, (pd - 1) % 4)) #gegen uhrzeigersinn drehen
    yield (1000 + total, (pr, pc, (pd + 1) % 4)) #im uhrzeigersinn drehen
    dr, dc = directions[pd]
    if grid[pr + dr][pc + dc] != "#":
        yield (1 + total, (pr + dr, pc + dc, pd))

def dijkstra(grid, start, end):
    heap = [(0, start)]
    best_costs = {start: 0}
    goBack = {}
    best_cost = float("inf")
    final_positions = set()
    while heap:
        total_cost, pos = heapq.heappop(heap)
        if total_cost > best_costs.get(pos, float("inf")):
            continue
        best_costs[pos] = total_cost
        cr, cc, _ = pos
        if (cr, cc) == end:
            if total_cost > best_cost:
                break
            best_cost = total_cost
            final_positions.add(pos)
        for cost, option in options(total_cost, pos, grid):
            best = best_costs.get(option, float("inf"))
            if cost > best:
                continue
            if cost < best:
                goBack[option] = set()
                best_costs[option] = cost
            goBack[option].add(pos)
            heapq.heappush(heap, (cost, option))
    return final_positions, goBack

final, goBack = dijkstra(grid, start, end)
positions = []
for pos in final:
    positions.append(pos)
seen = set(final)
while positions:
    pos = positions.pop()
    for prev in goBack.get(pos, []):
        if prev in seen:
            continue
        seen.add(prev)
        positions.append(prev)

unique_positions = {(r, c) for r, c, _ in seen}
print(len(unique_positions))

    