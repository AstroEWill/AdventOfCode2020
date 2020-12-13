dataFile = open("AOC_Day3.txt")
splitInfo = dataFile.read().split("\n")

def tobogganSlope(slopeX, slopeY):
    for i in range(0, len(splitInfo)):
        x = 0
        y = 0
        treeCount = 0

        while (y <= len(splitInfo) - (slopeY + 1)):
            x += slopeX
            y += slopeY

            if x >= (len(splitInfo[1])-slopeX):
                x -= len(splitInfo[1])

            if ((splitInfo[y][x]  == "#")):
                    treeCount += 1
    return treeCount

total = tobogganSlope(1, 1) * tobogganSlope(3, 1) * tobogganSlope(5, 1) * tobogganSlope(7, 1) * tobogganSlope(1, 2)
print(total)