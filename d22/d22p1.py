from math import floor
from functools import cache
with open("input.txt", "r") as file:
    initial_numbers = file.read().strip().splitlines()


def mix(x, y):
    return x ^ y

def prune(x):
    return x & 16777215
@cache
def processNumber(x):
    x = mix(x, x << 6)
    x = prune(x)
    x = mix(x, x >> 5)
    x = prune(x)
    x = mix(x, x << 11)
    x = prune(x)
    return x

result = 0

for num in initial_numbers:
    for _ in range(2000):
        num = processNumber(int(num))
    result += num
print(result)