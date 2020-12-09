numList = open("day9input").read().splitlines()
numList = list(map(int, numList))

p = 0
for num in numList:
    
    newP = p+25
    preamble = numList[p:newP]
    try:
        sumNum = numList[newP]
    except:
        break

    testFlag = 0
    for testNum in preamble:
        if (sumNum - testNum) in preamble:
            testFlag = 1
   
    if testFlag == 0:
        invalidNum = sumNum
    
    p = p+1

p = 0
testFlag = 0
for num in numList:
    if testFlag == 0:
        startNum = num
        sumNum = num
        for newNum in numList[p+1:len(numList)]:
            sumNum = sumNum + newNum
            if sumNum == invalidNum:
                endNum = newNum
                testFlag = 1
    p=p+1

startDex = numList.index(startNum)
endDex = numList.index(endNum)
endDex = endDex+1

contList = numList[startDex:endDex]
weakness = max(contList) + min(contList)
print(str(weakness)+" = "+str(max(contList))+" + "+str(max(contList)))



