

commandList = open("day8input").read().splitlines()



duplicate = 0
nList = []
n = 0
acc = 0
while duplicate == 0:

    if n not in nList:
        command = commandList[n].split(" ")[0]
        value = int(commandList[n].split(" ")[1])
        if command == "jmp":
            print(commandList[n])
            nList.append(n)
            n = n + value
        elif command == "acc":
            acc = acc + value
            print(commandList[n])
            nList.append(n)
            n = n+1
        else:
            print(commandList[n])
            n = n+1
    else:
        print(str(n))
        print(commandList[n])
        duplicate = 1

print("Accumulator value: "+str(acc))
    #check that line isn't duplicate
    #commands are nop, acc, jmp