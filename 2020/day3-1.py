

trackList = open("day3input").read().splitlines()


n = 0
trees = 0
for track in trackList:
    if track[n] == "#":
        trees = trees+1
    n = n+3
    if n > 30:
        n = n - 31
print("you accidentally "+str(trees)+" whole trees")
