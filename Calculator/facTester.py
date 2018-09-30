##print(type("Str"))
##if str == type("str"):
##    print("yes")
##from calc_methods import isFloat
##
##def putInNegs(string1, numOfNeg, indexList): #putInNegs(string, string.count("-"), list(filter(lambda x: string[x] == "-", range(len(string)))))
##    if numOfNeg == 0:
##        print(string1)
##        return string1
##    else:
##        currIndex = indexList[numOfNeg - 1]
##        print(string1[currIndex + 1])
##        if not isFloat(string1[currIndex + 1]):
##            newStr = string1[:currIndex + 1] + "1" + string1[currIndex + 1:]
##            print(newStr)
##        else:
##            newStr = string1
##        return putInNegs(newStr, numOfNeg - 1, indexList)
##
##string = "(-x-1)(-2x+1)"
##print(putInNegs(string, string.count("-"), list(filter(lambda x: string[x] == "-", range(len(string))))))
##string = "2x(x-2)(x+2)"
##tupList = [(string[:i].rfind("("), i) for i in range(len(string)) if string[i] == ")"]
##print(tupList)
##def findFactors(num):
##    #return list(filter(lambda x: num % x == 0, range(1, num + 1)))
##    l = list(filter(lambda x: num % x == 0, range(1, num + 1)))
##    if(len(l) % 2 == 1):
##        l.insert(int(len(l) / 2), l[int(len(l) / 2)])
##    return l
##
##def t(termsList):
##    lfacs = findFactors(abs(termsList[2]))
##    lfacs = [num * -1 for num in lfacs] + lfacs
##    lfacs.sort(reverse=True)
##    fterm = termsList[0]
##    addTerm = termsList[1]
##    lterm = termsList[2]
##    ffacs = findFactors(abs(termsList[0]))
##    ffacs = [num * -1 for num in ffacs] + ffacs
##    ffacs.sort(reverse=True)
##    for i in range(int(len(ffacs) / 4)): #efficient
##        fL = [ffacs[i], ffacs[int(len(ffacs)/2)-1-i], ffacs[int(len(ffacs)/2)+i], ffacs[len(ffacs)-1-i]]
##        if fterm > 0:
##            useL = [(fL[0], fL[1]), (fL[2], fL[3])]
##        else:
##            useL = [(fL[0], fL[2]), (fL[1], fL[3])]
##        #print(useL)
##        for tup in useL:
##            for i2 in range(int(len(lfacs) / 4)):
##                lL = [lfacs[i2], lfacs[int(len(lfacs)/2)-1-i2], lfacs[int(len(lfacs)/2)+i2], lfacs[len(lfacs)-1-i2]]
##                if lterm > 0:
##                    useL2 = [(lL[0], lL[1]), (lL[2], lL[3])]
##                else:
##                    useL2 = [(lL[0], lL[2]), (lL[1], lL[3])]
##                for tup2 in useL2:
##                    #print("(%d , %d)(%d , %d)" % (tup[0], tup2[0], tup[1], tup2[1]))
##                    if (tup2[0] * tup[1]) + (tup2[1] * tup[0]) == addTerm:
##                        return "(%dx+%d)(%dx+%d)" % (tup[0], tup2[0], tup[1], tup2[1])
##                    elif(tup[0] * tup2[0]) + (tup[1] * tup2[1]) == addTerm:
##                        return ("(%dx+%d)(%dx+%d)" % (tup[0], tup2[1], tup[1], tup2[0])).replace("+-", "-").replace("1x","x")
##
##print(t([36, 6, -6]))
