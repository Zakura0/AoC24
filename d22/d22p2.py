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
buyers_sequences = []
for num in initial_numbers:
    num = int(num)
    sequences = {}
    for _ in range(1997):
        temp = num
        old_price = temp % 10
        differences = []
        difference = 0
        for i in range(4):
            temp = processNumber(temp)
            price = temp % 10
            difference = price - old_price
            old_price = price
            differences.append(difference)
        if len(differences) == 4:
            sequence =  (differences[0], differences[1], differences[2], differences[3])
            if sequence not in sequences:
                sequences[sequence] = price
        num = processNumber(num)
    buyers_sequences.append(sequences)

test_dict = buyers_sequences[0]
for sequences in buyers_sequences[1:]:
    for sequence, price in sequences.items():
        if sequence in test_dict:
            test_dict[sequence] += price
        else:
            test_dict[sequence] = price

result = max(test_dict.values())
print(result)