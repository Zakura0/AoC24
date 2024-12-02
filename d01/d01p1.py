with open ("input.txt", "r") as file:
    numbers = list(map(int, file.read().split()))
left = numbers[::2]
right = numbers[1::2]
distance = 0
while left:
    distance += abs(min(left) - min(right))
    left.remove(min(left))
    right.remove(min(right))

print(distance)
