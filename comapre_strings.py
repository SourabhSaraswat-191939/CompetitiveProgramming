n = int(input())

for i in range(n):
    s = input()
    t = input()
    result = True
    countDict = {}
    for i in s:
        if i in countDict:
            countDict[i]+=1
        else:
            countDict[i]=1
    
    for i in t:
        if i in countDict:
            countDict[i]+=1
        else:
            countDict[i]=1

    for x in countDict:
        if countDict[x]%2!=0:
            result = False
            break
    if result:
        print("YES")
    else:
        print("NO")