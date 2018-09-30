def isFloat(st):
    try:
        float(st)
        return True
    except ValueError:
        return False
l = [1, 4, 4, 16]
l = [-1 * num for num in l] + l
print(l)
##ffacs = [1, 2, 4, 4, 8, 16]
##print(list(range(int(len(ffacs) / 2) - 1, -1,-1)))
##num = 8 ** (1/3)
##print(num)
#string1 = "-1*8.0"
#str1 = [char for i in len(string1) - 1 if char != "-" or (char == "-" and i > 0 and isFloat(string1[i - 1]) and isFloat(string1[i + 1])) else "_"]
##str1 = ""
##for i, char in enumerate(string1):
##    if char != "-" or (char == "-" and (i > 0 and isFloat(string1[i + 1])) and isFloat(string1[i - 1])):
##        str1 += char
##    else:
##        str1 += "_"
##print(str1)
##def switchDubNegs(string1):
##    return string1.replace("--", "+")
##def putInNegs(string1, numOfNeg, indexList): #putInNegs(string, string.count("-"), list(filter(lambda x: string[x] == "-", range(len(string)))))
##    print(indexList)
##    if numOfNeg == 0:
##        return string1
##    else:
##        currIndex = indexList[numOfNeg - 1]
##        if not isFloat(string1[currIndex + 1]):
##            newStr = string1[:currIndex + 1] + "1" + string1[currIndex + 1:]
##        else:
##            newStr = string1
##        return putInNegs(newStr, numOfNeg - 1, indexList)
##string_inputt = "-(4+4)"
##string = switchDubNegs(string_inputt)
##print(string)
##string = putInNegs(string, string.count("-"), list(filter(lambda x: string[x] == "-", range(len(string)))))
##print(string)
##string = "hello"
##print(string[0::-1])
##def convertUnderscores(string1):
##    str1 = ""
##    for i, charr in enumerate(string1):
##        if charr != "-" or (charr == "-" and (i > 0 and isFloat(string1[i + 1])) and isFloat(string1[i - 1])):
##            str1 += charr
##        else:
##            str1 += "_"
##    return str1

##string = "(-8.0)"
##print(convertUnderscores(string))
