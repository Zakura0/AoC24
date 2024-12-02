with open ("input.txt", "r") as file:
    numbers = list(map(int, file.read().split()))
left = numbers[::2]
right = numbers[1::2]
sum = 0
for i in range(len(left)):
    count = right.count(left[i])
    sum += left[i] * count

print(sum)