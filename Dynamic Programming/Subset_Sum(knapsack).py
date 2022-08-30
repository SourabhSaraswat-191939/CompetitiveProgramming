def isSubsetSum (N, arr, sum):
    dp = []
    # Approach 1 => Using Top Down
    for i in range(N+1):
        temp = []
        for j in range(sum+1):
            temp.append(-1)
        
        dp.append(temp)
    
    def find(i,w):
        if w==0:
            return True
        
        if i==0:
            return False
        
        if dp[i][w]!=-1:
            return dp[i][w]
            
        if w>=arr[i-1]:
            dp[i][w] = (find(i-1,w-arr[i-1]) or find(i-1,w))
        else:
            dp[i][w] = find(i-1,w)
        
        return dp[i][w]
    
    return find(N,sum)
    
    
    
    # Approach 2 => Using Bottom Up

    # for i in range(N+1):
    #     temp = []
    #     for j in range(sum+1):
    #         for j in range(sum+1):
                # temp.append(False)
        
    #     dp.append(temp)
    # dp[0][0] = True
    # for i in range(1,N+1):
    #     for j in range(1,sum+1):
    #         if arr[i-1]<=j:
    #             dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
    #         else:
    #             dp[i][j] = dp[i-1][j]
    
    # return dp[N][sum]

print(isSubsetSum(6,[3, 34, 4, 12, 5, 2],9))