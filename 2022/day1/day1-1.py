

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

print("Least Hungry Elf is:", max(calList))