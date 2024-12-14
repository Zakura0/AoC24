import numpy as np
import math

with open("input.txt", "r") as file:
    input = file.read().strip().split("\n\n")

machines = []
for block in input:
    block = block.splitlines()
    a = block[0].split("+")
    a = (int(a[1][:len(a[1]) - 3]), int(a[2]))
    b = block[1].split("+")
    b = (int(b[1][:len(b[1]) - 3]), int(b[2]))
    p = block[2].split("=")
    p = (int(p[1][:len(p[1]) - 3]) + 10000000000000, int(p[2]) + 10000000000000)
    machines.append([p, a, b])

# a[0] * n + b[0] * m = p[0]
# a[1] * n + b[1] * m = p[1]
def findCheapest(machine):
    a = machine[1]
    b = machine[2]
    p = machine[0]
    arr = np.array([[a[0], b[0]], [a[1], b[1]]])
    arr = np.long(arr)
    sol = np.array([p[0], p[1]])
    #sol = np.
    s = np.linalg.solve(arr, sol)
    n, m = s[0], s[1]
    decimaln = float("0." + str(n).split(".")[1])
    decimalm = float("0." + str(m).split(".")[1])
    if (decimalm < 0.01 or decimalm > 0.99) and (decimaln < 0.01 or decimaln > 0.99):
        return 3*round(n) + round(m)
    else:
        return 0
        

result = 0
for machine in machines:
    result += findCheapest(machine)
print(result)