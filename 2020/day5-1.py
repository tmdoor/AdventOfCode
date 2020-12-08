import string

seatList = open("day5input").read().splitlines()

#128 rows on plane
#8 columns
#RRRRRRRCCC

highSeat = 0
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
    if seatId > highSeat:
        highSeat = seatId

print("Highest seat ID is "+str(highSeat))