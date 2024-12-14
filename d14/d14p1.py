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

for _ in range(100):
    for i in range(len(robots)):
        robots[i] = move(robots[i])

quadrants = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}

def getQuadrant(x, y):
    if x < width // 2 and y < height // 2:
        return 1
    elif x > width // 2 and y < height // 2:
        return 2
    elif x < width // 2 and y > height // 2:
        return 3
    elif x > width // 2 and y > height // 2:
        return 4
    else:
        return 0

for robot in robots:
    x, y = robot[0]
    quadrant = getQuadrant(x, y)
    quadrants[quadrant] += 1

result = 1
for i in range(1, 5):
    result *= quadrants[i]
print(result)


