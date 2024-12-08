with open("input.txt", "r") as file:
    grid = file.read().strip().splitlines()

height = len(grid)
width = len(grid[0])

antennas = []

for x in range(height):
    for y in range(width):
        if grid[x][y] != ".":
            seen = set()
            antennas.append((grid[x][y], x, y, seen))

antinodes = set()

for antenna in antennas:
    for i in range(len(antennas)):
        if antenna == antennas[i]:
            continue
        if antenna[0] == antennas[i][0] and (antenna[1], antenna[2]) not in antennas[i][3]:
            distance = (antenna[1] - antennas[i][1], antenna[2] - antennas[i][2])
            double_distance = (distance[0] * 2, distance[1] * 2)
            flip_distance = (distance[0] * -1, distance[1] * -1)
            first = (antennas[i][1] + double_distance[0], antennas[i][2] + double_distance[1])
            second = (antennas[i][1] + flip_distance[0], antennas[i][2] + flip_distance[1])
            if 0 <= first[0] < height and 0 <= first[1] < width:
                antinodes.add(first)
            if 0 <= second[0] < height and 0 <= second[1] < width:
                antinodes.add(second)
            antenna[3].add((antennas[i][1], antennas[i][2]))
            antennas[i][3].add((antenna[1], antenna[2]))
print(len(antinodes))