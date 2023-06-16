import string

f = open("day3input", "r")

#construct dict with letter values
lettersList = string.ascii_lowercase + string.ascii_uppercase
lettersDict = {}
value = 1
for i in lettersList:
    lettersDict[i] = value
    value = value+1


#halve strings and compare to find duplicate
prioritySum = 0
for line in f:
    line = list(line)
    half = int(len(line)/2)
    comOne = line[0:half]
    comTwo = line[half:-1]
    for x in comOne:
        if x in comTwo:
            prioritySum += lettersDict[x]
            break

print(prioritySum)





