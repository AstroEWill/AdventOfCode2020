textFile = open("AOC_Day2.txt","r")


def part1():
    satisfiedPasswords = 0

    splitStrings = textFile.read().split('\n')

    for i in range(0, len(splitStrings)):
        split = splitStrings[i].split("-")
        lowBound = int(split[0])
        highBound = int(split[1].split(" ")[0])

        necessaryValue = split[1].split(" ")[1][0]

        repeatedCount = 0
        for j in range(7, len(splitStrings[i])):
            if splitStrings[i][j] == necessaryValue:
                repeatedCount += 1

        if (repeatedCount >= lowBound) and (repeatedCount <= highBound):
            satisfiedPasswords += 1

    print(satisfiedPasswords)

def part2():
    satisfiedPasswords = 0

    splitStrings = textFile.read().split('\n')

    for i in range(0, len(splitStrings)):
        splitVal = splitStrings[i].split("-")
        firstPosition = int(splitVal[0])
        secondPosition = int(splitVal[1].split(" ")[0])

        necessaryValue = splitVal[1].split(" ")[1][0]
        passwordString = splitVal[1].split(" ")[2]

        if (passwordString[firstPosition-1] == necessaryValue) or (passwordString[secondPosition-1] == necessaryValue):
            if (passwordString[firstPosition - 1] != (passwordString[secondPosition - 1])):
                satisfiedPasswords += 1

    print(satisfiedPasswords)
part2()
textFile.close()