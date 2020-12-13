dataFile = open("AOC_Day6.txt")
from collections import Counter

splitData = dataFile.read().split("\n\n")
splitData = [x.strip().split("\n") for x in splitData]

totalAnswers = 0

for answers in splitData:
    answeredQuestions = []
    for individualAnswer in answers:
        for character in individualAnswer:
            answeredQuestions.append(character)

    counts = Counter(answeredQuestions)
    duplicateValues = [char for char in answeredQuestions if counts[char] == len(answers)]

    answeredQuestions = []
    for i in duplicateValues:
        for char in i:
            if char not in answeredQuestions:
                answeredQuestions.append(char)

    totalAnswers += len(answeredQuestions)

print(totalAnswers)