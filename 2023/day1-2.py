from word2number import w2n



f = open('day1input')
list_of_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

sum = 0
for line in f:
    lineDict={}
    highInd = 0
    lowInd = 100
    for num in list_of_nums:
        #find first occurrence of a number
        index = line.find(num)
        if index != -1:
            lineDict[index] = str(w2n.word_to_num(num))
            if index > highInd:
                highInd = index
            if index < lowInd:
                lowInd = index
        #find last occurrence of a number, middle duplicates dont matter
        index = line.rfind(num)
        if index != -1:
            lineDict[index] = str(w2n.word_to_num(num))
            if index > highInd:
                highInd = index
            if index < lowInd:
                lowInd = index
    partSum = int(lineDict[lowInd] + lineDict[highInd])
    sum = sum + partSum

print(sum)


