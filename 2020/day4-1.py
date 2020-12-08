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

#find passports that fit criteria
validPassports = 0
for passDict in passDictList:
    if len(passDict) == 8:
        validPassports = validPassports + 1
    elif len(passDict) == 7:
        if "cid" not in passDict:
            validPassports = validPassports + 1
            
print(str(validPassports)+" passports are valid")