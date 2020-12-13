file = open("AOC_Day8.txt")

splitData = file.read().splitlines()
splitData = [x.strip().split(" ") for x in splitData]

def checkValidity(data):
    accumulator = 0
    instructionIndex = 0
    visitedInstructionIndexes = []
    breakValue = "Continue"
    while breakValue != "Break" and instructionIndex < (len(data) - 1):
        visitedInstructionIndexes.append(instructionIndex)

        if data[instructionIndex][0] == "acc":
            accumulator += int(data[instructionIndex][1])
            if (instructionIndex + 1) not in visitedInstructionIndexes:
                instructionIndex += 1
            else:
                breakValue = "Break"
        elif data[instructionIndex][0] == "jmp":
            if (instructionIndex + int(data[instructionIndex][1])) not in visitedInstructionIndexes:
                instructionIndex += int(data[instructionIndex][1])
            else:
                breakValue = "Break"
        elif data[instructionIndex][0] == "nop":
            if (instructionIndex + 1) not in visitedInstructionIndexes:
                instructionIndex += 1
            else:
                breakValue = "Break"

    if breakValue == "Break":
        return [False, accumulator]
    else:
        return [True, accumulator]

for i in range(len(splitData)):
    placeholder = splitData[:]
    print(placeholder)

    if placeholder[i][0] == "jmp":
        placeholder[i][0] = "nop"
    elif placeholder[i][0] == "nop":
        placeholder[i][0] = "jmp"

    checkVar = checkValidity(placeholder)
    if checkVar[0]:
        print(checkVar[1])
        break