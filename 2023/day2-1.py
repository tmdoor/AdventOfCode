


f = open('day2input')
sum = 0
for line in f:
    valid = 0
    line = line.strip()
    firstList = line.split(":") #split game x: blue x, red y; blue z, red w
    id = int(firstList[0].split()[-1])
    print("ID : "+str(id))
    gameStr = firstList[-1]
    setList = gameStr.split(";") #split blue x, red y; blue z, red w
    for set in setList:
        colorList = set.split(",") #split blue x, red y
        for color in colorList:
            cubes = color.split() #split blue x
            print(cubes)
            if cubes[1] == 'blue':
                if int(cubes[0]) > 14:
                    valid += 1
            if cubes[1] == 'red':
                if int(cubes[0]) > 12:
                    valid += 1
            if cubes[1] == 'green':
                if int(cubes[0]) > 13:
                    valid += 1
    if valid == 0:
        print(valid)
        sum = sum+id

print(sum)
