

commandList = open("day8input").read().splitlines()


def run_command(lineStr,fn,fAcc):
    #input: command, pointer, accumlator value
    #output: accumlator value, pointer
    command = lineStr.split(" ")[0]
    value = int(lineStr.split(" ")[1])
    if command == "jmp":
        nValue = value
        fn = fn + nValue
    elif command == "acc":
        fAcc = fAcc + value
        nValue = 1
        fn = fn+nValue
    else:
        nValue = 1
        fn = fn+nValue
    return [fAcc,fn,nValue]


solved = 0
testList = commandList.copy()
testednList = []
finalAcc = 0
while solved == 0:
    nList = []
    n = 0
    acc = 0

    #while loop iterates through instructions until it hits a loop, or it hits EOF without looping
    while (n not in nList) and (n<653):
        print
        nList.append(n)
        returnList = run_command(testList[n],n,acc)
        n = returnList[1]
        acc = returnList[0]
    else:
        #reset list change if loop encountered
        testList = commandList.copy()
        #set solved if reached EOF without loop
        if n >= 652:
            solved = 1
            finalAcc = acc
    
    testn = 0
    #goes through lines and changes to nop or jmp if it has not yet been tested
    for testCommand in testList:
        if testn not in testednList:
            if testCommand.split(" ")[0] == "jmp":
                testStr = "nop +0"
                testList[testn] = testStr
                testednList.append(testn)
                break
            elif testCommand.split(" ")[0] == "nop":
                testStr = "jmp "+testCommand.split(" ")[1]
                testList[testn] = testStr
                testednList.append(testn)
                break
            else:
                testn = testn+1
        else:
            testn = testn+1

print("Accumulator value: "+str(finalAcc))
