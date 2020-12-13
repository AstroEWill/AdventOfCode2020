dataFile = open("AOC_Day4.txt")
#dataFile = open("AOC_TestData.txt")

#SHOULD BE 121

splitData = dataFile.read().split("\n\n")
dictionaryCheck = {}
acceptableHCL = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "C", "d", "e", "f"]
eclList = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

j = 0
acceptedPassports = 0
metCriteria = 0

for element in splitData:
    splitData[j] = element.replace("\n"," ")
    j += 1

j = 0

for test in splitData:
    test.replace("\n", " ")

    splitData[j] = test.split(" ")

    j += 1

acceptedList = []

for element in splitData:
    for dataSet in element:
        key = dataSet[0:3]
        code = dataSet[4:len(dataSet)]
        if key == "byr":
            if len(code) == 4 and 1920 <= int(code) <= 2002:
                metCriteria += 1
            else:
                break
        elif key == "iyr":
            if len(code) == 4 and 2010 <= int(code) <= 2020:
                metCriteria += 1
            else:
                break
        if key == "eyr":
            if len(code) == 4 and 2020 <= int(code) <= 2030:
                metCriteria += 1
            else:
                break
        elif key == "hgt":
            if code[-1] == "m":
                if 150 <= int(code[0:len(code)-2]) <= 193:
                    metCriteria += 1
                else:
                    break
            elif code[-1] == "n":
                if 59 <= int(code[0:len(code)-2]) <= 76:
                    metCriteria += 1
                else:
                    break
        elif key == "hcl":
            if code[0] == "#":
                if len(code) == 7:
                    validChar = 0
                    for char in code[1:len(code)]:
                        if char in acceptableHCL:
                            validChar += 1
                        else:
                            break
                    if validChar == 6:
                        metCriteria += 1
                else:
                    break
            else:
                break

        elif key == "ecl":
            if code in eclList:
                metCriteria += 1
            else:
                break
        elif key == "pid":
            if len(code) != 9 or code[0] not in acceptableHCL[0:9]:
                break
            if len(code) == 9:
                try:
                    int(code)
                except ValueError:
                    break
                else:
                    metCriteria += 1
            else:
                break
    if metCriteria == 7:
        acceptedPassports += 1
    metCriteria = 0
    acceptedList.append(element)

print(acceptedList)
print("There are " + str(acceptedPassports) + " accepted passports.")
