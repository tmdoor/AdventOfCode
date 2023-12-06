f = open('day2input')
sum = 0
for line in f:
    line = line.strip()
    firstList = line.split(":") #split game x: blue x, red y; blue z, red w
    id = int(firstList[0].split()[-1])
    gameStr = firstList[-1]
    setList = gameStr.split(";") #split blue x, red y; blue z, red w

    highBlue = None
    highRed = None
    highGreen = None
    for set in setList:
        colorList = set.split(",") #split blue x, red y
        for color in colorList:
            cubes = color.split() #split blue x
            if cubes[1] == 'blue':
                if highBlue == None or int(cubes[0]) > highBlue:
                    highBlue = int(cubes[0])
            if cubes[1] == 'red':
                if highRed == None or int(cubes[0]) > highRed:
                    highRed = int(cubes[0])
            if cubes[1] == 'green':
                if highGreen == None or int(cubes[0]) > highGreen:
                    highGreen = int(cubes[0])

    power = highBlue * highRed * highGreen
    sum = sum + power

print(sum)