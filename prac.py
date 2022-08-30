def maxMoves(s, t):
    word = s
    result = 0
    countLR = 0
    while result!=-1:
        result = word.find(t)
        if result==-1:
            break
        word = word[:result] + word[result+len(t):]
        countLR += 1
    
    countRL = 0
    result = 0
    s = s[::-1]
    while result!=-1:
        result = s.find(t)
        if result==-1:
            break
        s = s[:result] + s[result+len(t):]
        countRL += 1
    return max(countRL,countLR)

print(maxMoves("souararbh","rar"))