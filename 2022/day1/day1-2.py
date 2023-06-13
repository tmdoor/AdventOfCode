f = open("day1input", "r")

calList = []
calCount = 0
#sum lines, add sum to list when blank line
for line in f:
    if line != "\n":
        calCount = calCount + int(line)
    else:
        calList.append(calCount)
        calCount = 0

#find top three values and sum

n = 1
topThreeSum = 0
while n < 4:
    topThreeSum = topThreeSum + max(calList)
    calList.remove(max(calList))
    n += 1

print(topThreeSum)