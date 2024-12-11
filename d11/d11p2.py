from math import floor, log10
with open("input.txt", "r") as file:
    stones = file.read().strip().split(" ")

stones = [int(stone) for stone in stones]

def getLength(int):
    return floor(log10(int)) + 1 if int > 0 else 1

def splitEvenInt(int, length):
    divisor = 10 ** (length // 2)
    left = int // divisor
    right = int % divisor
    return left, right

cache = {}
def processStone(stone, blinks):
    if blinks == 0:
        return 1
    blinks = blinks - 1
    if (stone, blinks) in cache:
        return cache[stone, blinks]
    if stone == 0:
        childs = processStone(1, blinks)
        cache[stone, blinks] = childs
        return childs
    length = getLength(stone)
    if length % 2 == 0:
        left, right = splitEvenInt(stone, length)
        childs = processStone(left, blinks) + processStone(right, blinks)
        cache[stone, blinks] = childs
        return childs
    childs = processStone(stone * 2024, blinks)
    cache[stone, blinks] = childs
    return childs

result = 0
for stone in stones:
    result += processStone(stone, 75)

print(result)

            