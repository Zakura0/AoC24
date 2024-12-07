with open("input.txt", "r") as file:
    input = file.read().strip().splitlines()

def concat_int(x, y):
    return int("".join(str(num) for num in [x, y]))

def allSolutions(nums):
    if len(nums) == 1:
        return{nums[0]}
    subset = allSolutions(nums[:-1])
    multiplication = {num * nums[-1] for num in subset}
    addition = {num + nums[-1] for num in subset}
    concat = {concat_int(num, nums[-1]) for num in subset}
    return multiplication | addition | concat

sum = 0
for line in input:
    value, nums = line.split(": ")
    value = int(value)
    nums = [int(num) for num in nums.split(" ")]
    solutions = allSolutions(nums)
    #print(len(solutions)) #sollte 3^anzahl der Zahlen - 1 sein
    if value in solutions:
        sum += value
print(sum)




