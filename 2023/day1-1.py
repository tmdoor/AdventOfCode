

sum = 0
f = open('day1input')
for line in f:
    numList = []
    for char in line:
        if char.isnumeric():
            numList.append(char)
    num = int(numList[0]+numList[-1])
    sum = sum + num
print(sum)