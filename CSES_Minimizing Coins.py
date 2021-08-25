length, n = map(int,input().split())
arr = list(map(int,input().split()))
dp = [10000000]*(n+1)
dp[0]=0

for i in range(1,n+1):
    for j in range(length):
        if i-arr[j]>=0:
            dp[i] = min(dp[i], 1 + dp[i-arr[j]])

if dp[n] == 10000000:
    print(-1)
else: print(dp[n])

