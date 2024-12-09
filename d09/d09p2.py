with open("input.txt", "r") as file:
    line = file.read().strip()

def convertLine(line):
    result = ""
    index = 0
    for i in range(len(line)):
        num = line[i]
        if i % 2 == 0:
            result += str(num) + "*" + str(index) + ","
            index += 1
        else:
            if num != "0":
                result += "." * int(num) + ","
    result = result[:-1]
    result = result.split(",")
    return result

def sortLine(line):
    for i in range(1, len(line) + 1):
        last = line[-i]
        if last.startswith("."):
            continue
        amount = int(last[0])
        for j in range(len(line)):
            if len(line) - i < j:
                break
            if line[j].startswith("."):
                if amount <= len(line[j]):
                    line[-i] = "." * amount
                    rem = len(line[j]) - amount
                    if rem > 0:
                        dots = rem * "."
                        line.insert(j + 1, dots)
                    line[j] = last
                    break
            else:
                continue
    return line
        
def evaluateLine(line):
    result = 0
    index = 0
    for element in line:
        if element.startswith("."):
            index += len(element)
            continue
        amount, number = map(int, element.split("*"))
        for _ in range(amount):
            result += index * number
            index += 1
    return result

converted = convertLine(line)
sorted = sortLine(converted)
print(evaluateLine(sorted))
