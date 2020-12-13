file = open("AOC_Day9.txt")

lines = [l.rstrip('\n') for l in file]


lowIndex = 0
highIndex = 25

def analyze(lowIndex, highIndex):
    currentValues = lines[lowIndex:highIndex]

    targetVal = int(lines[highIndex])

    for val1 in currentValues:
        for val2 in currentValues:
            if val1 == val2:
                continue
            elif int(val1) + int(val2) == targetVal:
                return 0

    return targetVal

def checkWeakness(target, highIndex):
    for i in range(0,highIndex):
        currentTotal = int(lines[i])
        for j in range(i + 1, highIndex):
            if currentTotal == target:
                print(int(min(lines[i:j])) + int(max(lines[i:j])))
                return 0
            elif currentTotal > int(target):
                break
            else:
                currentTotal += int(lines[j])

while True:
    funcVal = int(analyze(lowIndex, highIndex))
    lowIndex += 1
    highIndex += 1

    if funcVal != 0:
        break

while True:
    check = checkWeakness(funcVal, highIndex)
    if check == 0:
        break
