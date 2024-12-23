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
    best_prices = set()
    difference = 0
    for _ in range(2000):
        num = processNumber(int(num))
        ones_digit = num % 10
        best_prices.add(ones_digit)
    sorted_prices = sorted(best_prices, reverse=True)
    print(sorted_prices)