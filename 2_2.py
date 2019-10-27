a = int(input())
b = int(input())
if a > 0:
    aStr = str(a)
    aList = list(aStr)
    aList = sorted(aList, reverse=True)
    aStr = ''.join(aList)

else:
    a = abs(a)
    aStr = str(a)
    aList = list(aStr)
    aList = sorted(aList)
    for x in aList:
        if x != 0:
            firstSign = x
            break
        else:
            aList = aList.pop()
    aNumberList = x + aList
    aNumberStr = aNumberList.join
    a = int(aNumberStr)

if b > 0:
    bStr = str(b)
    bList = list(bStr)
    bList = sorted(bList)
    bStr = ''.join(bList)


else:
    b = abs(b)
    bStr = str(b)
    bList = list(bStr)
    bList = sorted(bList, reverse=True)
    for x in bList:
        if x != 0:
            firstSign = x
            break
        else:
            bList = bList.pop()
    bNumberList = x + bList
    bStr = ''.join(bNumberList)

a = int(aStr)
b = int(bStr)
print(a - b)
