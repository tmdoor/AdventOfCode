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
        print(str(sumNum))
    
    p = p+1
        