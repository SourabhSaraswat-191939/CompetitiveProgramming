heights = [30,10, 60, 10, 60, 50]

length = len(heights)
dp = [-1]*(length+1)
dp[0] = 0
dp[1]= abs(heights[1]-heights[0])
def totalCost(N):
    if dp[N]!=-1:
        return dp[N]
    ans = min(totalCost(N-1) + abs(heights[N]-heights[N-1]), totalCost(N-2) + abs(heights[N]-heights[N-2]))
    dp[N] = ans
    return ans

print(totalCost(length-1))