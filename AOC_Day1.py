textFile = open("AOC_Day1.txt","r")
numList = []

inputFile = textFile.read().split("\n")
for values in inputFile:
    intValue = int(values)
    numList.append(intValue)

def dayOfCode():
    for i in range(0, len(numList)-1):
        currentValue = numList[i]
        for j in range(0,len(numList)-1):
            for k in range(0, len(numList) - 1):
                if (j != i) and (k != i) and (k != j):
                    if (numList[i] + numList[j] + numList[k] == 2020):
                        print(numList[i] * numList[j] * numList[k])
                        return


dayOfCode()
textFile.close()
