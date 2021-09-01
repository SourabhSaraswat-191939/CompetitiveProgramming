length, x = map(int,input().split())
coins = list(map(int,input().split()))
mode = 1000000007 
dp = [0]*(x+1)
dp[0]=1

for i in range(1,x+1):
    for j in range(length):
        if coins[j]>i: continue
        dp[i] = (dp[i] + dp[i-coins[j]])%mode
        
print(dp[x]%mode)

