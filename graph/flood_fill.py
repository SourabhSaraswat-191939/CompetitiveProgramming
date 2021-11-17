# using dfs

def floodFill(grid,sr,sc,newColor):
    print(grid,sr,sc,newColor)
    height = len(grid)
    width = len(grid[0])
    if (sr<0 or sc<0 or sr>=height or sc>=width or grid[sr][sc]==newColor or grid[sr][sc]!=change):
        return
    grid[sr][sc]=newColor
    xDir = [-1,1,0,0]
    yDir = [0,0,-1,1]
    for i in range(4):
        floodFill(grid,sr+xDir[i],sc+yDir[i],newColor)
    return

sr = 1
sc = 1
grid = [[1,1,1],[1,1,0],[1,0,1]]
change = grid[sr][sc]
floodFill(grid, sr, sc, 2)
print(grid)




# Using BFS
# from collections import deque

# sr = 1
# sc = 1
# grid = [[0,0,0],[0,1,1]]
# newColor = 1
# change = grid[sr][sc]
# height = len(grid)
# width = len(grid[0])

# def fill(grid,sr,sc,newColor):
#     if (sr<0 or sc<0 or sr>=height or sc>=width or grid[sr][sc]==newColor or grid[sr][sc]!=change):
#         return False
#     grid[sr][sc]=newColor
#     return True
# queue = deque()
# queue.append([sr,sc])
# grid[sr][sc]=newColor
# while queue:
#     print("Run ",queue)
#     out = queue.popleft()
#     sr = out[0]
#     sc = out[1]
#     xDir = [-1,1,0,0]
#     yDir = [0,0,-1,1]
#     for i in range(4):
#         if fill(grid,sr+xDir[i],sc+yDir[i],newColor):
#             queue.append([sr+xDir[i],sc+yDir[i]])
# print(grid)