class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        def dfs(grid, r, c):
            if (r>=height or c>=width or r<0 or c<0 or grid[r][c]!="1"):
                return
            grid[r][c] = "0"
            xDir = [-1,1,0,0]
            yDir = [0,0,-1,1]
            for i in range(4):
                dfs(grid,r+xDir[i],c+yDir[i])

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    dfs(grid,i,j)
                    result+=1
        return result