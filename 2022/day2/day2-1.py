import string

f = open("day2input", "r")

#points for specific choices"
valueDict = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}
#rock paper scissors results, 6 win, 3 draw, 0 loss
resultDict = {
    "A Y": 6,
    "B Z": 6,
    "C X": 6,
    "A X": 3,
    "B Y": 3,
    "C Z": 3,
    "A Z": 0,
    "B X": 0,
    "C Y": 0,
}

pointsSum = 0
for line in f:
    line = line.strip()
    points = resultDict[line] + valueDict[line[2]]
    pointsSum = pointsSum + points

print(pointsSum)