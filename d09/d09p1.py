with open("input.txt", "r") as file:
    line = file.read().strip()

def convertLine(line):
    result = ""
    index = 0
    for i in range(len(line)):
        num = line[i]
        if i % 2 == 0:
            result += int(num) * (str(index) + ",")
            index += 1
        else:
            result += ".," * int(num)
    result = result[:-1]
    result = result.split(",")
    return result

def sortLine(line):
    for i in range(1, len(line) + 1):
        if line[-i] == ".":
            continue
        index = line.index(".")
        if len(line) - i < index:
            break
        last = line[-i]
        line[index] = last
        line[-i] = "."
    return(line)

def evaluateLine(line):
    result = 0
    for i in range(len(line)):
        if line[i] == ".":
            return result
        result += i * int(line[i])

converted = convertLine(line)
sorted = (sortLine(converted))
print(evaluateLine(sorted))
