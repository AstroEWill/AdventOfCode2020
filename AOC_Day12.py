file = open("AOC_Day12.txt")
import math
# Not 3899
# Higher than 1676
splitData = list(l.strip("\n") for l in file)

# Heading: 1 = North, 2 = East, 3 = South, 4 = West
heading = 2
vertPos = 0
sidePos = 0
waypointY = 1
waypointX = 10

for navInstruc in splitData:
    instruction = navInstruc[0]
    magnitude = int(navInstruc[1:len(navInstruc)])
    tempWaypointX = waypointX
    tempWaypointY = waypointY

    if instruction == "R" or instruction == "L":
        theta = math.radians(magnitude)

    if instruction == "R":
        waypointX = tempWaypointX * math.cos(theta) + tempWaypointY * math.sin(theta)
        waypointY = -1 * tempWaypointX * math.sin(theta) + tempWaypointY * math.cos(theta)

        if magnitude == 90:
            heading += 1
        elif magnitude == 180:
            heading += 2
        elif magnitude == 270:
            heading += 3

    elif instruction == "L":
        if magnitude == 90:
            heading -= 1
        elif magnitude == 180:
            heading -= 2
        elif magnitude == 270:
            heading -= 3

        waypointX = tempWaypointX * math.cos(theta) - tempWaypointY * math.sin(theta)
        waypointY = tempWaypointX * math.sin(theta) + tempWaypointY * math.cos(theta)

    if heading > 4:
        heading -= 4
    elif heading < 1:
        heading += 4

    if instruction == "N":
        waypointY += magnitude
    elif instruction == "S":
        waypointY -= magnitude
    elif instruction == "E":
        waypointX += magnitude
    elif instruction == "W":
        waypointX -= magnitude
    elif instruction == "F":
        vertPos += waypointY * magnitude
        sidePos += waypointX * magnitude

print(round(abs(vertPos)) + round(abs(sidePos)))