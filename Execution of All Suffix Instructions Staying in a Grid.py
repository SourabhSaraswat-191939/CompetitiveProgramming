def executeInstructions(n, startPos, s):
    ans = []
    reset = startPos.copy()
    dirX = {'L':-1,'R':1,'U':0,'D':0}
    dirY = {'L':0,'R':0,'U':-1,'D':1}
    for i in range(len(s)):
        count = 0
        startPos = reset.copy()
        for j in range(i,len(s)):
            # print("startPos[1]",startPos[1],"; dirX[s[j]]",dirX[s[j]])
            if startPos[0]+dirY[s[j]]<0 or startPos[1]+dirX[s[j]]<0 or startPos[1]+dirX[s[j]]>=n or startPos[0]+dirY[s[j]]>=n:
                print("Error at ",i<0, j<0, i>=n, j>=n)
                break
            count+=1
            startPos[0]  += dirY[s[j]]
            startPos[1]  += dirX[s[j]]

            print("i",i,"j",j,"count",count)
            print(startPos)
        print("-----------------")            
        ans.append(count)
        
    return ans

print(executeInstructions(3,[0,1],"RRDDLU"))