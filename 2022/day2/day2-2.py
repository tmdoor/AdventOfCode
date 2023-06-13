import string

f = open("day2input", "r")

#points for win/loss/draw"
valueDict = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}
#points based on choice needed to win/lose/draw
resultDict = {
    "A Y": 1,
    "B Z": 3,
    "C X": 2,
    "A X": 3,
    "B Y": 2,
    "C Z": 1,
    "A Z": 2,
    "B X": 1,
    "C Y": 3,
}

pointsSum = 0
for line in f:
    line = line.strip()
    points = resultDict[line] + valueDict[line[2]]
    pointsSum = pointsSum + points

print(pointsSum)