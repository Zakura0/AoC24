with open("input.txt", "r") as file:
    blocks = file.read().strip().split("\n\n")

grid = blocks[0].splitlines()
instructions = "".join(blocks[1].splitlines())

height = len(grid)
width = len(grid[0])
robot = (0, 0)
obstacles = set()
walls = set()

for r in range(height):
    for c in range(width):
        if grid[r][c] == "@":
            robot = (r, c)
        elif grid[r][c] == "O":
            obstacles.add((r, c))
        elif grid[r][c] == "#":
            walls.add((r, c))
        else:
            continue

def printGrid(robot, obstacles, walls):
    for i in range(height):
        string = ""
        for j in range(width):
            if (i, j) == robot:
                string += "@"
            elif (i, j) in obstacles:
                string += "O"
            elif (i, j) in walls:
                string += "#"
            else:
                string += "."
        print(string)

def move(pos, dir):
    global robot
    rr, rc = pos
    dr, dc = dir
    if (rr + dr, rc + dc) not in walls:
        if (rr + dr, rc + dc) in obstacles:
            if rr == rr + dr:
                i = rc
                while True:
                    i += dc
                    if (rr, i) in obstacles:
                        continue
                    elif (rr, i) in walls:
                        break
                    else:
                        while True:
                            if i - dc == rc:
                                robot = (rr, i)
                                break
                            obstacles.remove((rr, i - dc))
                            obstacles.add((rr, i))
                            i -= dc                            
                        break
            else:
                i = rr
                while True:
                    i += dr
                    if (i, rc) in obstacles:
                        continue
                    elif (i, rc) in walls:
                        break
                    else:
                        while True:
                            if i - dr == rr:
                                robot = (i, rc)
                                break
                            obstacles.remove((i - dr, rc))
                            obstacles.add((i, rc))
                            i -= dr                            
                        break
        else:
            robot = (rr + dr, rc + dc) 

for arrow in instructions:
    if arrow == "<":
        move(robot, (0, -1))
    elif arrow == ">":
        move(robot, (0, 1))
    elif arrow == "^":
        move(robot, (-1, 0))
    elif arrow == "v":
        move(robot, (1, 0))

result = 0
for obstacle in obstacles:
    x, y = obstacle
    result += 100 * x + y

print(result)



    