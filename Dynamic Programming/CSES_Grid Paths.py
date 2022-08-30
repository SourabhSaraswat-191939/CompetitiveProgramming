n = int(input())
arr = []
mod = 10000000007
for i in range(n):
    arr.append(list(input()))

dp = []
for i in range(n):
    dp1 = []
    for j in range(n):
        dp1.append(0)
    dp.append(dp1)

if arr[n-1][n-1]=='.': dp[n-1][n-1]=1

for col in range(n-2,-1,-1):
    if arr[n-1][col]=='*':
        dp[n-1][col] == 0
    else:
        dp[n-1][col] += dp[n-1][col+1]

for row in range(n-2,-1,-1):
    if arr[row][n-1]=='*':
        dp[row][n-1] == 0
    else:
        dp[row][n-1] += dp[row+1][n-1]

for row in range(n-2,-1,-1):
    for col in range(n-2,-1,-1):
        if arr[row][col]=='*':
            dp[row][col] = 0
        else:
            dp[row][col] += (dp[row+1][col]%mod + dp[row][col+1]%mod)%mod
print(dp[0][0])