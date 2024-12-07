with open("input.txt", "r") as file:
    input = file.read().strip().splitlines()

def checkSolvable(value, nums):
    if len(nums) == 1:
        return value == nums[0]
    cut_nums = nums[:-1]
    if len(nums) > 0 and value % nums[-1] == 0:
        div = value // nums[-1]
        if checkSolvable(div, cut_nums):
            return True
    if len(nums) > 0 and value > nums[-1]:
        sub = value - nums[-1]
        if checkSolvable(sub, cut_nums):
            return True
    return False

sum = 0
for line in input:
    value, nums = line.split(": ")
    value = int(value)
    nums = [int(num) for num in nums.split(" ")]
    if checkSolvable(value, nums):
        sum += value

print(sum)



