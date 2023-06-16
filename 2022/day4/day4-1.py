f = open("day4input", "r")


def rangeify(rLine):
    rLine = rLine.split(",")
    range1 = rLine[0].split("-")
    range1 = range(int(range1[0]),int(range1[1]))
    range2 = rLine[1].split("-")
    range2 = range(int(range2[0]),int(range2[1]))
    return range1, range2

def compareRange(range1, range2):
    if range1.start >= range2.start and range1.stop <= range2.stop:
        return True
    elif range2.start >= range1.start and range2.stop <= range1.stop:
        return True
    else:
        return False    
 
overlapCount = 0
for line in f:
    range1, range2 = rangeify(line)
    if compareRange(range1, range2):
        overlapCount += 1
        
print(overlapCount)
