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
            robot = (r, c*2)
        elif grid[r][c] == "O":
            obstacles.add((r, c*2))
        elif grid[r][c] == "#":
            walls.add((r, c*2))
            walls.add((r, c*2 + 1))

def convertGrid(robot, obstacles, walls):
    converted = []
    for i in range(height):
        row = []
        for j in range(width * 2):
            if (i, j) == robot:
                row.append("@")
            elif (i, j) in obstacles:
                row.append("[")
            elif (i, j - 1) in obstacles:
                row.append("]")
            elif (i, j) in walls:
                row.append("#")
            else:
                row.append(".")
        converted.append(row)
    return converted

convertedGrid = convertGrid(robot, obstacles, walls)

def printGrid(grid):
    for i in range(height):
        string = ""
        for j in range(width * 2):
            string += grid[i][j]
        print(string)

def move(pos, dir):
    global convertedGrid
    global robot
    r, c = pos
    dr, dc = dir
    check = [pos]
    blocked = False
    for cr, cc in check:
        nr, nc = cr + dr, cc + dc
        if (nr, nc) in check:
            continue
        target = convertedGrid[nr][nc]
        if target == "#":
            blocked = True
            break
        if target == "[":
            check.append((nr, nc))
            check.append((nr, nc + 1))
        if target == "]":
            check.append((nr, nc))
            check.append((nr, nc - 1))
    if blocked:
        return
    copy_grid = [list(row) for row in convertedGrid]
    convertedGrid[r][c] = "."
    for obsr, obsc in check[1:]:
        convertedGrid[obsr][obsc] = "."
    for obsr, obsc in check[1:]:
        convertedGrid[obsr + dr][obsc + dc] = copy_grid[obsr][obsc]
    convertedGrid[r + dr][c + dc] = "@"
    robot = (r + dr, c + dc)

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
for r in range(height):
 for c in range(width * 2):
     if convertedGrid[r][c] == "[":
         result += 100 * r + c
        
print(result)


        



    