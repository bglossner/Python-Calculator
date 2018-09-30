from calc_methods import convertUnderscores
from calc_methods import findFullNum
from calc_methods import putInNegs

def floatToInt(numStr):
    num = float(numStr)
    if float(num) == int(num):
        return int(num)
    else:
        num = round(num, 3)
        return num
    
def findZeroes(string):
    zeroList = []
    ind = string.find("x")
    if string[ind + 1] == "(":
        zeroList.append("0")
    string = putOnes(string)
    string = putInNegs(string, string.count("-"), list(filter(lambda x: string[x] == "-", range(len(string)))))       
    tupList = [(string[:i].rfind("("), i) for i in range(len(string)) if string[i] == ")"]
    strList = [string[tup[0] + 1:tup[1]] for tup in tupList]
    for st in strList:
        zeroList.append(str(floatToInt(findZero(st))))
    return zeroList

def findZero(string):
    string = convertUnderscores(string)
    sN = int(findFullNum(string, 0, len(string)))
    fN = int(findFullNum(string, 1, -1))
    sN *= -1
    zero = sN / fN
    return str(zero)

def putOnes(string):
    holdStr = string
    while string.count("x") > 0:
        ind = string.find("x")
        if string[ind - 1] == "(":
            string = string[:ind] + "1" + string[ind:]
            string = string.replace("x", "y", 1)
        else:
            string = string.replace("x", "y", 1)
    return string.replace("y", "x")
