import calc_methods
import math

def facOutNum(numTerms):
    gDiv = numTerms[0]
    for i in range(1, len(numTerms)):
        gDiv = math.gcd(gDiv, numTerms[i])
    if gDiv > 1:
        return ([int(num / gDiv) for num in numTerms], str(gDiv))
    return (numTerms, str(gDiv))

def facOutX(facStr, numTerms):
    if len(numTerms) == 2 and facStr.endswith("x"):
        for num in numTerms:
            if facStr[facStr.index(str(num)) + len(str(num))] != "x":
                return False
        return True
    return False

def findFactors(num):
    l = list(filter(lambda x: num % x == 0, range(1, num + 1)))
    if(len(l) % 2 == 1):
        l.insert(int(len(l) / 2), l[int(len(l) / 2)])
    return l

def doTri(termsList):
    lfacs = findFactors(abs(termsList[2]))
    fterm = termsList[0]
    addTerm = termsList[1]
    lterm = termsList[2]
    if termsList[0] == 1:
        for i in range(int(len(lfacs) / 2)):
            firstNum, secondNum = lfacs[i], lfacs[len(lfacs) - i - 1]
            if firstNum + secondNum == abs(addTerm) or (addTerm == 0 and lterm > 0):
                tup = (firstNum, secondNum) if addTerm > 0 else (-1 * firstNum, -1 * secondNum)
            else:
                tup = (firstNum * -1, secondNum) if addTerm > 0 else (firstNum, secondNum * -1)
            if tup[0] + tup[1] == addTerm:
                return ("(x+%d)(x+%d)" % tup).replace("+-", "-")
        return None
    else:
        ffacs = findFactors(abs(termsList[0]))
        ffacs = [num * -1 for num in ffacs] + ffacs
        ffacs.sort(reverse=True)
        lfacs = [num * -1 for num in lfacs] + lfacs
        lfacs.sort(reverse=True)
        for i in range(int(len(ffacs) / 4)): #efficient
            fL = [ffacs[i], ffacs[int(len(ffacs)/2)-1-i], ffacs[int(len(ffacs)/2)+i], ffacs[len(ffacs)-1-i]]
            if fterm > 0:
                useL = [(fL[0], fL[1]), (fL[2], fL[3])]
            else:
                useL = [(fL[0], fL[2]), (fL[1], fL[3])]
            for tup in useL:
                for i2 in range(int(len(lfacs) / 4)):
                    lL = [lfacs[i2], lfacs[int(len(lfacs)/2)-1-i2], lfacs[int(len(lfacs)/2)+i2], lfacs[len(lfacs)-1-i2]]
                    if lterm > 0:
                        useL2 = [(lL[0], lL[1]), (lL[2], lL[3])]
                    else:
                        useL2 = [(lL[0], lL[2]), (lL[1], lL[3])]
                    for tup2 in useL2:
                        if (tup2[0] * tup[1]) + (tup2[1] * tup[0]) == addTerm:
                            return (("(%dx+%d)(%dx+%d)" % (tup[0], tup2[0], tup[1], tup2[1])).replace("+-", "-")).replace("1x","x")
                        elif(tup[0] * tup2[0]) + (tup[1] * tup2[1]) == addTerm:
                            return (("(%dx+%d)(%dx+%d)" % (tup[0], tup2[1], tup[1], tup2[0])).replace("+-", "-")).replace("1x","x")
        return None

def doFactor(facStr):
    facStr = facStr.lower()
    facLen = len(facStr)
    if "^" not in facStr:
        return facStr
    facSt = facStr.replace("^2", "^^")
    holdFac = facSt[::-1]
    if holdFac.find("^^") < holdFac.rfind("^") - 1: #this is dumb way to do it
        return "Can't factor above ^2"
    facNeg = calc_methods.convertUnderscores(facSt)
    numOfTerms = facStr.count("x") + 1
    indexList = list(filter(lambda x: facStr[x] == "x", range(facLen)))
    numTerms = [int(calc_methods.findFullNum(facNeg, 0, i)) for i in indexList if i != 0]
    if indexList[0] == 0:
        numTerms.insert(0, 1)
        facSt = "1" + facSt
    if not facStr.endswith("x"): #could be facSt[facLen - 1] == x or facStr[-1:] == x 
        numTerms.append(int(calc_methods.findFullNum(facNeg, 0, facLen)))
    holdTerms = numTerms.copy()
    tupGCD = facOutNum(numTerms)
    numTerms = tupGCD[0]
    gDiv = tupGCD[1]
    if gDiv != "1":
        for i, term in enumerate(numTerms):
            facSt = facSt.replace(str(holdTerms[i]), str(term), 1)
    if facOutX(facSt, numTerms):
        return (gDiv + ("x(x+%d)" % numTerms[-1])).replace("+-", "-")  if gDiv != "1" else ("x(x+%d)" % numTerms[-1]).replace("+-", "-")
    if numOfTerms == 3:
        answer = doTri(numTerms)
    if numOfTerms == 2 and "^2" in facStr:
        numTerms.insert(1, 0)
        answer = doTri(numTerms)
    if gDiv != "1":
        return gDiv + answer
    return answer
