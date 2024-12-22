from itertools import product
with open("input.txt", "r") as file:
    lines = file.read().strip().splitlines()

big_keypad = [["7", "8", "9"],
              ["4", "5", "6"],
              ["1", "2", "3"],
              [".", "0", "A"]]

robot_keypad = [[".", "^", "A"],
                ["<", "v", ">"]]

def getAllMoves(keypad, string):
    height = len(keypad)
    width = len(keypad[0])
    key_positions = {}
    for row in range(height):
        for col in range(width):
            if keypad[row][col] != ".":
                key_positions[keypad[row][col]] = (row, col)
    key_moves = {}
    for key1 in key_positions:
        for key2 in key_positions:
            if key1 == key2:
                key_moves[(key1, key2)] = ["A"]
                continue
            possible_moves = []
            queue = [(key_positions[key1], "")]
            shortest = 10000
            while queue:
                pos, way = queue.pop(0)
                r, c = pos
                for nr, nc, sign in [(r - 1, c, "^"), (r + 1, c, "v"), (r, c - 1, "<"), (r, c + 1, ">")]:
                    if 0 <= nr < height and 0 <= nc < width:
                        if keypad[nr][nc] != ".":
                            if keypad[nr][nc] == key2:
                                if shortest < len(way) + 1:
                                    break
                                shortest = len(way) + 1
                                possible_moves.append(way + sign + "A")
                            else:
                                queue.append(((nr, nc), way + sign))
                else:
                    continue
                break
            key_moves[(key1, key2)] = possible_moves
    combinations = [key_moves[(key1, key2)] for key1, key2 in zip("A" + string, string)]
    moves = ["".join(combination) for combination in product(*combinations)]
    return moves

result = 0

for line in lines:
    robot1_moves = getAllMoves(big_keypad, line)

    maybe_moves = []
    for move in robot1_moves:
        maybe_moves += getAllMoves(robot_keypad, move)
    min_length = min(len(move) for move in maybe_moves)
    robot2_moves = [move for move in maybe_moves if len(move) == min_length]

    maybe_moves = []
    for move in robot2_moves:
        maybe_moves += getAllMoves(robot_keypad, move)
    min_length = min(len(move) for move in maybe_moves)
    robot3_moves = [move for move in maybe_moves if len(move) == min_length]

    numeric_part = int(''.join(filter(str.isdigit, line)))

    result += min_length * numeric_part

print(result)


    
    
    
    
        
                      

        
