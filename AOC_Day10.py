file = open("AOC_Day10.txt")

voltageList = [int(l.rstrip('\n')) for l in file]
voltageList.sort()
currentVoltage = 0
oneVDif = 0
threeVDif = 1
print(voltageList)

for voltage in voltageList:
    if (voltage - currentVoltage) == 1:
        oneVDif += 1
    elif (voltage - currentVoltage) == 3:
        threeVDif += 1

    currentVoltage += (voltage - currentVoltage)

print(oneVDif * threeVDif)
