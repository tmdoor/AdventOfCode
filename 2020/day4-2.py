#open file, replace newline with spaces, split into list on double space (empty lines in file)
passList = open("day4input").read().replace("\n"," ").split("  ")


#construct the list of passport dicts
passDictList = []
for passport in passList:
    passDict = {}
    passport = passport.split(" ")
    for field in passport:
        keyVal = field.split(":")[0]
        valVal = field.split(":")[1]
        passDict[keyVal] = valVal
    passDictList.append(passDict)

#construct list of valid passport dicts
validPassports = []
for passDict in passDictList:
    if len(passDict) == 8:
        validPassports.append(passDict)
    elif len(passDict) == 7:
        if "cid" not in passDict:
            validPassports.append(passDict)

extraValidPassports = 0
#verify validity of eligible passports
eyeList = ["amb","blue","brn","gry","grn","hzl","oth"]
for passDict in validPassports:
    invalidPass = 0
    
    #check that applicable value lengths are correct number of digits
    byrLen = len(passDict["byr"])
    iyrLen = len(passDict["iyr"])
    eyrLen = len(passDict["eyr"])
    pidLen = len(passDict["pid"])
    lenProd = byrLen*iyrLen*eyrLen*pidLen
    if lenProd != 576:
        invalidPass = 1
    
    #check that values above are in valid ranges
    if int(passDict["byr"]) not in  range(1920,2002):
        invalidPass = 1
    if int(passDict["iyr"]) not in  range(2010,2020):
        invalidPass = 1
    if int(passDict["eyr"]) not in  range(2020,2030):
        invalidPass = 1
    
    #check that height is right format and value
    if passDict["hgt"][-2:] == "cm":
        if int(passDict["hgt"][:-2]) not in range(150,193):
            invalidPass = 1
    elif passDict["hgt"][-2:] == "in":
        if int(passDict["hgt"][:-2]) not in range(59,76):
            invalidPass = 1
    else:
        invalidPass = 1

    #check if hair color is valid hex by trying to convert to int
    if len(passDict["hcl"]) != 7:
        invalidPass = 1
    if passDict["hcl"][0] == "#":
        try:
            testInt = int(passDict["hcl"][1:])
        except:
            invalidPass = 1
    else:
        invalidPass = 1

    #check if eye color is valid
    if passDict["ecl"] not in eyeList:
        invalidPass = 1
    
    if invalidPass == 0:
        extraValidPassports = extraValidPassports+1
        print(passDict)







print(str(extraValidPassports)+" passports are valid")