

trackList = open("day3input").read().splitlines()



totalTrees = 1
skipList = [1,3,5,7]
for skip in skipList:
    n = 0
    trees = 0
    for track in trackList:
        if track[n] == "#":
            trees = trees+1
        n = n+skip
        if n > 30:
            n = n - 31
    totalTrees = totalTrees * trees

n=0
trees = 0
lineSkip = 0
for track in trackList:
    if lineSkip == 0:
        if track[n] == "#":
            trees = trees+1
        n = n+1
        if n > 30:
            n = n - 31
        lineSkip = 1
    else:
        lineSkip = 0

totalTrees = totalTrees * trees

print("you accidentally "+str(totalTrees)+" trees")
