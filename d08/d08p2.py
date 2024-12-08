with open("input.txt", "r") as file:
    grid = file.read().strip().splitlines()

grid = [list(line) for line in grid]
height = len(grid)
width = len(grid[0])

antennas = []

for x in range(height):
    for y in range(width):
        if grid[x][y] != ".":
            seen = set()
            antennas.append((grid[x][y], x, y))

antinodes = set()

for antenna in antennas:
    for i in range(len(antennas)):
        if antenna == antennas[i]:
            continue
        if antenna[0] == antennas[i][0]:
            distance = (antenna[1] - antennas[i][1], antenna[2] - antennas[i][2])
            mult = 1
            mult_distance = (distance[0] * mult, distance[1] * mult)
            node = (antennas[i][1] + mult_distance[0], antennas[i][2] + mult_distance[1])
            for _ in range(2):
                while 0 <= node[0] < height and 0 <= node[1] < width:
                    antinodes.add(node)
                    mult += 1
                    mult_distance = (distance[0] * mult, distance[1] * mult)
                    node = (antennas[i][1] + mult_distance[0], antennas[i][2] + mult_distance[1])
                distance = (distance[0] * -1, distance[1] * -1) #flip
print(len(antinodes))
flip_distance = (distance[0] * -1, distance[1] * -1)