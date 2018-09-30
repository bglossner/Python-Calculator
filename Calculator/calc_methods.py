import math

def isFloat(s):
    try:
        float(s)
        return True
    except:
        return False

def findFullNum(string, step, index): #this could be done more simply, just messin around with some stuff
    l1 = list(filter(lambda x: not isFloat(x) and x != "." and x != "_", string[index - 1::-1]) if step == 0 else filter(lambda x: not isFloat(x) and x != "." and x != "_", string[index + 1:len(string)]))
    if len(l1) != 0:
        indexOfSign = string.rfind(l1[0], 0, index - 1) if step == 0 else string.find(l1[0], index + 1, len(string))
    else:
        indexOfSign = -1 if step == 0 else len(string)
    string = string.replace("_", "-")
    return string[indexOfSign + 1:index] if step == 0 else string[index + 1: indexOfSign]

def convertUnderscores(string1):
    str1 = ""
    for i, charr in enumerate(string1):
        if charr != "-" or (charr == "-" and (i > 0 and isFloat(string1[i + 1])) and isFloat(string1[i - 1])):
            str1 += charr
        else:
            str1 += "_"
    return str1

def putInNegs(string1, numOfNeg, indexList): #putInNegs(string, string.count("-"), list(filter(lambda x: string[x] == "-", range(len(string)))))
    if numOfNeg == 0:
        return string1
    else:
        currIndex = indexList[numOfNeg - 1]
        if not isFloat(string1[currIndex + 1]):
            newStr = string1[:currIndex + 1] + "1" + string1[currIndex + 1:]
        else:
            newStr = string1
        return putInNegs(newStr, numOfNeg - 1, indexList)
