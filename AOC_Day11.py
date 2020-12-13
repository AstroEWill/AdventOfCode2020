file = open("AOC_Day11.txt")

infoGrid = [list(l.strip("\n")) for l in file]
stability = 0

def gridLocalCheck(lineInfo):
    changedGrid = []
    placeholderList = lineInfo
    for row in range(len(lineInfo)):
        placeholderRow = ''
        for column in range(len(lineInfo[0])):
            localSeats = []
            for x in (-1, 0, 1):
                for y in (-1, 0, 1):
                    if x == y == 0:
                        continue
                    i = 1
                    #if 0 <= row+x < len(lineInfo) and 0 <= column + y < len(lineInfo[0]):
                    #    localSeats.append(placeholderList[row+x][column+y])

                    while 0 <= row + i*x < len(lineInfo) and 0 <= column + i*y < len(lineInfo[0]):
                        currentStatus = placeholderList[row+i*x][column+i*y]

                        if currentStatus != ".":
                            localSeats.append(currentStatus)
                            break
                        i += 1

            if lineInfo[row][column] == "L" and "#" not in localSeats:
                placeholderRow += "#"
            elif lineInfo[row][column] == "#" and localSeats.count("#") >= 5:
                placeholderRow += "L"
            else:
                placeholderRow += lineInfo[row][column]
        changedGrid.append(placeholderRow)

    return changedGrid

while stability != 1:
    modifiedGrid = gridLocalCheck(infoGrid)

    if modifiedGrid == infoGrid:
        print("".join(modifiedGrid).count("#"))
        break

    infoGrid = modifiedGrid

