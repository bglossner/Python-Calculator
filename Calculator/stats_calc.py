import math
global listDic
listDic = {}

def strLToI(l):
    if type(l[0] == str):
        l = [int(item) for item in l]
        return l
    else:
        return l

def getSum(l):
    l = strLToI(l)
    total = 0
    for num in l:
        total += num
    return total

def getMean(l):
    l = strLToI(l)
    tSum = getSum(l)
    return tSum / len(l)

def getVariance(l):
    l = strLToI(l)
    mean = getMean(l)
    l = list(map(lambda x: (x-mean) ** 2, l)) #[(num - mean) ** 2 for num in l]
    return getMean(l)

def getStdDev(l):
    l = strLToI(l)
    return math.sqrt(getVariance(l))

def getMedian(l):
    l = strLToI(l)
    l.sort()
    ll = len(l)
    if len(l) % 2 == 0:
        return getMean([l[int((ll / 2) - 1)], l[int(ll / 2)]])
    return l[int(ll / 2)]

def getRange(l):
    l = strLToI(l)
    return max(l) - min(l)

def getMakeList():
    print("Lists are: " + ", ".join(listDic.keys()))
    l = input("\nName the list: ")
    ele = input("Set elements (put spaces between each element) or use lists: ")
    listDic[l] = ele.split()

def getEditList():
    print("Lists are: " + ", ".join(listDic.keys()))
    lEdit = input("Which list would you like to edit? ")
    print("\n%s is currently set to: [%s]" % (lEdit, ", ".join(listDic[lEdit])))
    st = input("Edit whole list ('Yes') or select indexes ('Sel') or add numbers ('Add')\nor delete numbers ('Del') or change list by constant ('con change'): ")
    if st == "Yes":
        print("Editing %s list" % lEdit)
        listDic[lEdit] = input("Elements (separate by spaces): ").split()
    elif st == "Sel":
        l = input("\nPut in indexes you'd like changed (start = 1): ").split()
        l2 = input("What would you like to change indexes %s to, respectively? " % ", ".join(l)).split()
        for i, num in enumerate(l):
            listDic[lEdit][int(num) - 1] = l2[i]
    elif st == "Add":
        l = input("\nEnter what you'd like to add with spaces between: ").split()
        listDic[lEdit].extend(l)
    elif st == "Del":
        l = input("\nWhich indexes would you like to delete (start=1)? ").split()
        l.sort(reverse=True)
        for num in l:
            del listDic[lEdit][int(num) - 1]
    elif st == "con change":
        changeStr = input("Use 'l' for list, operator, and constant (2-l, l+1): ")
        for i, num in enumerate(listDic[lEdit]):
            change = changeStr.replace("l", num)
            listDic[lEdit][i] = str(eval(change))
        
    print("\nList %s is now: [%s]" % (lEdit, ", ".join(listDic[lEdit])))

def getDeleteList():
    print("Lists are: " + ", ".join(listDic.keys()))
    lEdit = input("Which list would you like to delete? ")
    del listDic[lEdit]
