import string

seatList = open("day5input").read().splitlines()

highSeat = 0
idList = []
for seat in seatList:

    #construct binary strings for row and column
    rowStr = seat[:7]
    rowStr = rowStr.replace("F","0")
    rowStr = rowStr.replace("B","1")
    columnStr = seat[7:]
    columnStr = columnStr.replace("L","0")
    columnStr = columnStr.replace("R","1")

    row = int(rowStr, 2)
    column = int(columnStr, 2)

    seatId = (row * 8) + column
    idList.append(seatId)

idList.sort()
yourList = []
prevId = 0
#find skips in list, your seat will be the seatID in yourList-1
for seatId in idList:
    if (seatId - prevId) > 1:
        yourList.append(seatId)
    prevId = seatId

print(yourList) 