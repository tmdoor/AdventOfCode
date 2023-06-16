import string

f = open("day3input", "r")

#construct dict with letter values
lettersList = string.ascii_lowercase + string.ascii_uppercase
lettersDict = {}
value = 1
for i in lettersList:
    lettersDict[i] = value
    value = value+1


lineCount = 1
prioritySum = 0
lineList = []
for line in f:
    line = list(line)
    #add three lines at a time to list for comparison
    if lineCount < 3:
        lineList.append(line)
        lineCount += 1
    elif lineCount == 3:
        lineList.append(line)
        #compare elements of three lines
        print(lineList)
        for x in lineList[0]:
            if x in lineList[1]:
                if x in lineList[2]:
                    prioritySum += lettersDict[x]
                    break
        lineList = []
        lineCount = 1

print(prioritySum)