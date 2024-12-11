with open("input.txt", "r") as file:
    stones = file.read().strip().split(" ")

stones = [int(stone) for stone in stones]

def blink(stones):
    new_stones = []
    for i in range(len(stones)):
        if stones[i] == 0:
             new_stones.append(1)
        elif len(str(stones[i])) % 2 == 0:
            string = str(stones[i])
            left = int(string[:len(string) // 2])
            right = int(string[len(string) // 2:])
            new_stones.append(left)
            new_stones.append(right)
        else:
            new_stones.append(stones[i] * 2024)
    return new_stones

for i in range(25):
    stones = blink(stones)

print(len(stones))

            