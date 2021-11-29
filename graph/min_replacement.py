from collections import deque
def minReplacement(grid):
    r = len(grid)
    c = len(grid[0])
    q = deque()
    visited = set()
    xDir = [-1,1,0,0]
    yDir = [0,0,-1,1]
    q.append((0,0,0))   # (x point, y point, weight till that point)
    while q:
        curr = q.popleft()
        visited.add((curr[0],curr[1]))
        if curr[0]==r-1 and curr[1]==c-1:
            return curr[2]
        for i in range(4):
            x = curr[0]+xDir[i]
            y = curr[1]+yDir[i]
            if x<0 or y<0 or x>=r or y>=c:
                continue
            if (x,y) in visited:
                continue
            cost =0
            if grid[curr[0]][curr[1]]=='U' and xDir[i]==-1:
                cost = 0
            elif grid[curr[0]][curr[1]]=='D' and xDir[i]==1:
                cost = 0
            elif grid[curr[0]][curr[1]]=='L' and yDir[i]==-1:
                cost = 0
            elif grid[curr[0]][curr[1]]=='R' and yDir[i]==1:
                cost = 0
            else:
                cost = 1
            if cost==1:
                q.append((x,y,curr[2]+1))
            else:
                q.appendleft((x,y,curr[2]))
        
    return -1 

g = [['R','R','D'],['L','D','L'],['U','R','R']]
result = minReplacement(g)
print(result)