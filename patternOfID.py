def smallestNumber(pattern):
    n=len(pattern)
    count = [0]*(n+1)
    # count[0] = 
    for i in range(n):
        co=0
        if i<n-1:
            j=i
            while j<n and pattern[j]=='D':
                co+=1
                j+=1
            
        count[i] = co
    occur = set()
    maxi = 1+count[0]
    result = str(maxi)
    for i in range(n):
        if pattern[i]=='I':
            maxi+=1
            print(i,maxi,"->",maxi+count[i+1])
            maxi += count[i+1]
            result+=str(maxi+count[i+1])
            # maxi+=count[i+1]
            
        else:
            result+=str(int(result[-1])-1)
        
    print(count)
    return result

print(smallestNumber("IIIDIDDD"))