with open("input.txt", "r") as file:
    lines = file.read().strip().splitlines()

lines = [line.split("p=")[1].split("v=") for line in lines]
robots = []
height = 103
width = 101
for line in lines:
    robot = []
    for element in line:
        parts = element.split(",")
        x, y = int(parts[0]), int(parts[1])
        robot.append((x, y))
    robots.append(robot)

def move(robot):
    px, py = robot[0]
    mx, my = robot[1]
    px = (px + mx) % width
    py = (py + my) % height
    return [(px, py), (mx, my)]

def getLargestComponent(positions):
    seen = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    largest_component = 0
    for pos in positions:
        if pos in seen:
            continue
        x, y = pos
        seen.add(pos)
        queue = [pos]
        component_size = 1
        while queue:
            x, y = queue.pop()
            component_size += 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx and nx < width and 0 <= ny and ny < width:
                    if (nx, ny) in positions and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        queue.append((nx, ny))
        if largest_component < component_size:
            largest_component = component_size
    return largest_component

def printPositions(positions):
    for i in range(101):
        string = ""
        for j in range(103):
            if (j, i) in positions:
                string += "X"
            else:
                string += "."
        print(string + "\n")
        
largest = 0
for i in range(1, 10000):
    positions = set()
    for j in range(len(robots)):
        robots[j] = move(robots[j])
        positions.add(robots[j][0])
    comp = getLargestComponent(positions)
    if largest < comp:
        largest = comp
        index = i
    if i == 7672:
        printPositions(positions)

print(index, largest)


