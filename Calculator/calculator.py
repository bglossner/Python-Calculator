print("\nWelcome to Ben's Calculator")
print("No PEMDAS\n")
isDone = False

def convertUnderscores(string1):
    str1 = ""
    for i, charr in enumerate(string1):
        if charr != "-" or (charr == "-" and (i > 0 and isFloat(string1[i + 1])) and isFloat(string1[i - 1])):
            str1 += charr
        else:
            str1 += "_"
    print("Neg Underscores: " + str1)
    return str1

def switchDubNegs(string1):
    return string1.replace("--", "+")

def findFullNum(string, step, index): #this could be done more simply, just messin around with some stuff
    #print(string[index - 1::-1])
    l1 = list(filter(lambda x: not isFloat(x) and x != "." and x != "_", string[index - 1::-1]) if step == 0 else filter(lambda x: not isFloat(x) and x != "." and x != "_", string[index + 1:len(string)]))
##    foundSign = False
##    while not foundSign:
##        if len(l1) != 0:
##            indexOfSign = string.rfind(l1[0], 0, index - 1) if step == 0 else string.find(l1[0], index + 1, len(string))
##            if isFloat(string[indexOfSign - 1]) and isFloat(string[indexOfSign + 1])
##        else:
    print("List of different operators, except one being tested: ", end="")
    print(l1)
    if len(l1) != 0:
        indexOfSign = string.rfind(l1[0], 0, index - 1) if step == 0 else string.find(l1[0], index + 1, len(string))
    else:
        indexOfSign = -1 if step == 0 else len(string)
##    if :
##        return "-" + string[indexOfSign + 1:index] if step == 0 else "-" + string[index + 1: indexOfSign]
##    else:
##        return string[indexOfSign + 1:index] if step == 0 else string[index + 1: indexOfSign]
    print("Index of next operator: %d" % indexOfSign)
    string = string.replace("_", "-")
    return string[indexOfSign + 1:index] if step == 0 else string[index + 1: indexOfSign]

def findNumsLR(string1, char, *arg):
    #print(arg)
    str1 = ""
    for i, charr in enumerate(string1):
        if charr != "-" or (charr == "-" and (i > 0 and isFloat(string1[i + 1])) and isFloat(string1[i - 1])):
            str1 += charr
        else:
            str1 += "_"
    print(str1)
    index = str1.index(char)
    firstNum = findFullNum(str1, 0, index)
    secondNum = findFullNum(str1, 1, index)
    return list([firstNum, secondNum])
    
def moreMultChar(indexList, string1, index):
    if(index == len(indexList)):
        return string1
    else:
        currIndex = indexList[index]
        opList = ["+","-","*","/"]
        if isFloat(string1[currIndex - 1]) or string1[currIndex -1] == ")" and string1[currIndex - 1] not in opList and currIndex != 0:
            newStr = string1[:currIndex] + "*" + string1[currIndex:len(string1)]
            indexList = [num + 1 for num in indexList] #list comprehension!
        else:
            newStr = string1
        return moreMultChar(indexList, newStr, index + 1)

def addMultChar(string1, numParens): #need to drastically change
    indexList = []
    indexList.append(string1.index("("))
    for i in range(numParens - 1):
        indexList.insert(0, indexList[0] + 1 + string1[indexList[0] + 1:len(string1)].index("("))
    indexList.sort()
    return moreMultChar(indexList, string1, 0)

def putInNegs(string1, numOfNeg, indexList): #putInNegs(string, string.count("-"), list(filter(lambda x: string[x] == "-", range(len(string)))))
    if numOfNeg == 0:
        print(string1)
        return string1
    else:
        currIndex = indexList[numOfNeg - 1]
        print(string1[currIndex + 1])
        if not isFloat(string1[currIndex + 1]):
            newStr = string1[:currIndex + 1] + "1" + string1[currIndex + 1:]
            print(newStr)
        else:
            newStr = string1
        return putInNegs(newStr, numOfNeg - 1, indexList)
    
def returnFullMainList(numstr):
    symIndex = 0
    symChar = ""
    for i, char in enumerate(numstr):
        if(not(isFloat(char)) and char != "."):
            if char == "-":
                if i > 0 and isFloat(numstr[i - 1]) and isFloat(numstr[i + 1]):
                    symIndex = i
                    symChar += char
                    break
            else:
                symIndex = i
                symChar += char
                break
            
    firstNum = float(numstr[:symIndex])
    secondNum = float(numstr[symIndex + 1:len(numstr)])
    return list([symChar, symIndex, firstNum, secondNum])

def mainFunc(str_input):
    str1 = "".join(str_input.split())
    str = switchDubNegs(str1)
    print(str)
    ansList = returnFullMainList(str)
    print(ansList)
    symChar = ansList[0]
    symIndex, firstNum, secondNum = ansList[1], ansList[2], ansList[3]
    return ansFun(symChar, symIndex, firstNum, secondNum)

def ansFun(*args):
    symChar = args[0]
    symIndex, firstNum, secondNum = args[1], args[2], args[3]
    answer = 0
    print("First Num: " + str(firstNum) + ". Second Num: " + str(secondNum) + ", " + symChar)
    firstNum = float(firstNum) if type(firstNum) != float else firstNum
    secondNum = float(secondNum) if type(secondNum) != float else secondNum
    #print(firstNum, secondNum)
    if(symChar == "+"):
        answer = addFunc(firstNum, secondNum)
    elif(symChar == "-"):
        answer = subtractFunc(firstNum, secondNum)
    elif(symChar == "*"):
        answer = multFunc(firstNum, secondNum)
    elif(symChar == "/"):
        answer = divFunc(firstNum, secondNum)
    else:
        answer = exponFunc(firstNum, secondNum)
    #print(answer)
    return answer

def isFloat(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False
    
def addFunc(num1, num2):
    return num1 + num2
#f = lambda x, y: x + y; g = f(2, 3)
def subtractFunc(num1, num2):
    return num1 - num2
def multFunc(num1, num2):
    return num1 * num2
def divFunc(num1, num2):
    return float(num1) / num2
def exponFunc(num1, num2):
    return num1 ** num2
#Start
while not isDone:
    string_inpu = input("Two nums and a symbol: ")
    if string_inpu == "done":
        print("Terminating")
        exit()
    elif(string_inpu != "d"):
        print("Answer is: %.3f!\nRounded to two decimals.\n" % mainFunc(string_inpu))
    else:
        isDone = True

isDone = False

def makeDict(my_str):
    dictOfChars = {"+":0, "-":0, "*":0, "/":0, "^":0}
    for char in my_str:
        for key in dictOfChars:
            if(char == str(key)):
                dictOfChars[key] += 1
                break
    print(dictOfChars)
    return dictOfChars;

newNum = 0

def findExclusiveIndex(str):
    opCompStr = "+-*/^"
    tempList = []
    for i, char in enumerate(str):
        if char in opCompStr:
            if len(tempList) == 1:
                return i
            else:
                tempList.append(i)
    return tempList[0]
                
def recurseVal(numStr, numOfOps, opList):
    str_to_replace = ""
    if numOfOps == 0:
        return numStr
    else:
        if numOfOps == 1:
            str_to_replace += numStr;
        else:
            str_to_replace += numStr[:findExclusiveIndex(numStr)]
        
        del opList[0]
        newNum = mainFunc(str_to_replace)
        return recurseVal(str(newNum) + numStr.replace(str_to_replace, "", 1), numOfOps - 1, opList)
    
def makeOPList(string_input):
    opList = []
    for i, char in enumerate(string_input):
            opCompStr = "+-*/^"
            if char in opCompStr:
                opList.append(i)
    return opList

while not isDone:
    string_inp = input("Multi-Operation Evaluator: ")
    if string_inp == "done":
        print("Terminating")
        exit()
    string_input = "".join(string_inp.split())
    opList = makeOPList(string_input)
    if(string_input != "d"):
        value = float(recurseVal(string_input, len(opList), opList))
        print("Answer is: %.3f!\nRounded to two decimals.\n" % value)
    else:
        isDone = True
        
isDone = False
        
def makeParenList(numStr):
    parenList = []
    parenList.append(numStr.index(")"))
    parenList.append(numStr[:parenList[0]].rfind("("))
    print("Parenthesis Indexes: %d, %d" % (parenList[1], parenList[0]))
    return parenList

def doExponents(numStr):
    str_to_replace = ""
    count = numStr.count("^")
    if count == 0:
        return numStr
    else:
        l1 = findNumsLR(numStr, "^")
        str_to_replace += l1[0] + "^" + l1[1]
        return testFunc(numStr, doExponents, str_to_replace, ansFun("^", 0 , l1[0], l1[1]))
        
def doMultDiv(numStr):
    str_to_replace = ""
    char = ""
    count=numStr.count("*") + numStr.count("/")
    if count == 0:
        return numStr
    else:
        if((numStr.find("*") < numStr.find("/") and numStr.find("*") != -1) or numStr.find("/") == -1):
            char = "*"
            l1 = findNumsLR(numStr, "*")
            str_to_replace += l1[0] + "*" + l1[1]
            return testFunc(numStr, doMultDiv, str_to_replace, ansFun(char, 0 , l1[0], l1[1]))
        else:
            char = "/"
            l1 = findNumsLR(numStr, "/")
            str_to_replace += l1[0] + "/" + l1[1]
            return testFunc(numStr, doMultDiv, str_to_replace, ansFun(char, 0 , l1[0], l1[1]))
        
def doAddSub(numStr):
    str_to_replace = ""
    char = ""
    count = numStr.count("+") + numStr.count("-")
    if count == 0:
        return numStr
    else:
        if((numStr.find("+") < numStr.find("-") and numStr.find("+") != -1) or numStr.find("-") == -1):
            char = "+"
            l1 = findNumsLR(numStr, "+")
            str_to_replace += l1[0] + "+" + l1[1]
            return testFunc(numStr, doAddSub, str_to_replace, ansFun(char, 0 , l1[0], l1[1]))
        else:
            strHold = convertUnderscores(numStr)
            if strHold.count("-") == 0:
                return numStr
            char = "-"
            l1 = findNumsLR(numStr, "-")
            str_to_replace += l1[0] + "-" + l1[1]
            return testFunc(numStr, doAddSub, str_to_replace, ansFun(char, 0 , l1[0], l1[1])) #check this line out, then the return function on testFunc
        
def testFunc(numStr, string, str_to_replace, newNumb):
    #strin = [string]
    #print(numStr)
    newStr = numStr.replace(str_to_replace, str(newNumb), 1)
    return string(newStr) #map(lambda x: x(newStr), strin)
    
def goThruPEMDAS(numStr):
    l1=[numStr]
    listOfCounts = makeDict(numStr)
    #print(listOfCounts)
    #newStr = doAddSub(doMultDiv(doExponents(numStr) if listOfCounts["^"] > 0 else numStr) if listOfCounts["*"] > 0 or listOfCounts["/"] > 0) if listOfCounts["+"] > 0 or listOfCounts["-"] > 0 else newStr
    if(listOfCounts["^"] > 0):
        #print("h")
        l1.insert(0, doExponents(l1[0]))
        print(l1[0])
    if(listOfCounts["*"] > 0 or listOfCounts["/"] > 0):
        l1.insert(0, doMultDiv(l1[0]))
        print(l1[0])
    if(listOfCounts["+"] > 0 or listOfCounts["-"] > 0):
         l1.insert(0, doAddSub(l1[0]))
         print(l1[0])
    return str(l1[0])
    
def pemdasEval(numStr, numParen):
    if numParen > 0:
        #print(numStr)
        parenList = makeParenList(numStr)
        str_to_replace = numStr[parenList[1] + 1:parenList[0]]
        valueInParen = goThruPEMDAS(str_to_replace)
        numStr2 = numStr.replace("(" + str_to_replace + ")", valueInParen, 1)
        #print(numParen)
        return pemdasEval(numStr2, numParen - 1)
    else:
        return numStr
        
while not isDone:
    string_inp = input("\nMulti-Operation Evaluator with PEMDAS: ")
    if string_inp == "done":
        print("Terminating")
        exit()
    if(string_inp != "d"):
        string_inputt = "".join(string_inp.split())
        string_inputt += ")"
        numParenSet = string_inputt.count("(") + 1
        string = switchDubNegs(string_inputt)
        string = putInNegs(string, string.count("-"), list(filter(lambda x: string[x] == "-", range(len(string)))))
        if(numParenSet > 1):
            string = addMultChar(string, numParenSet - 1)
        #else:
 #           string = string_inputt
        string_input = "(" + string
        print(string_input)
        value = float(pemdasEval(string_input, numParenSet))
        print("Answer is: %.3f!\nRounded to two decimals.\n" % value)
    else:
        isDone = True
        
        
print("Calculator program terminated")
