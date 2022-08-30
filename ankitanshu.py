res = []
def countConnected(grid):
    height = len(grid)
    width = len(grid[0])
    def dfs(grid, r, c, count,parent):
        if (r>=height or c>=width or r<0 or c<0 or grid[r][c]!=1):
            return 0      
        grid[r][c] = 0
        xDir = [-1,1,0,0]
        yDir = [0,0,-1,1]
        for i in range(4):
            count+=dfs(grid,r+xDir[i],c+yDir[i],count,False)
        count+=1
        if parent:
            # print(r,c,count)
            res.append(count)
            return 0
        return count
    result = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                dfs(grid,i,j,0,True)
                result+=1
    return result

n=int(input())
m=int(input())
arr = []
for _ in range(m):
    arr.append(list(map(int,input().split())))
countConnected(arr)
res.sort()
flag = False
ans = 0
for val in res:
    if flag:
        ans+=val
        flag=False
    else:
        flag=True
print(ans)