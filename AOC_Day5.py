dataFile = open("AOC_Day5.txt")

seatData = dataFile.read().split("\n")
maxSeatID = 0
seatList = []

for element in seatData:
    seatRows = list(range(0, 128))
    seatColumns = list(range(0, 8))

    for char in element[0:7]:
        if char == "F":
            del seatRows[-int(len(seatRows)/2):]
        elif char == "B":
            del seatRows[:int(len(seatRows)/2)]

    for char in element[7:10]:
        if char == "R":
            del seatColumns[:int(len(seatColumns)/2)]
        elif char == "L":
            del seatColumns[int(len(seatColumns)/2):]


    seatID = seatRows[0] * 8 + seatColumns[0]

    '''
    if seatID > maxSeatID:
        maxSeatID = seatID
    '''
    seatList.append(seatID)

    '''
    for i in range(0, len(seatList) - 1):
        if (seatList[i] + 1) != seatList[i+1] or seatList[i] - 1 != seatList[i-1]:
            print("Seat ID is " + str(seatList[i]))
    '''
seatList.sort()

for val in range(seatList[0], seatList[-1]):
    if val not in seatList:
        if (val - 1) not in seatList or (val + 1) not in seatList:
            pass
        else:
            print(val)