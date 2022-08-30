from collections import deque
import time

def floodFill(grid,sr,sc,newColor):
    if (sr<0 or sc<0 or sr>=height or sc>=width or grid[sr][sc]==newColor or grid[sr][sc]!=change):
        return
    grid[sr][sc]=newColor
    xDir = [-1,1,0,0]
    yDir = [0,0,-1,1]
    for i in range(4):
        floodFill(grid,sr+xDir[i],sc+yDir[i],newColor)
    
    for row in grid:
        for i in row:
            print(i if i!='' else ' ',end='')
        print()
    time.sleep(0.3)

grid = []

# For making heart shape
# define size n = even only
n = 14
  
# so this heart can be made n//2 part left,
# n//2 part right, and one middle line
# i.e; columns m = n + 1
m = n+1
  
# loops for upper part
for i in range(n//2-1):
    grid.append([])
    for j in range(m):
          
        # condition for printing stars to upper line
        if i == n//2-2 and (j == 0 or j == m-1):
            grid[i].append('❤️')
            print("❤️", end=" ")
              
        # condition for printing stars to left upper
        elif j <= m//2 and ((i+j == n//2-3 and j <= m//4) \
                            or (j-i == m//2-n//2+3 and j > m//4)):
            print("❤️", end=" ")
            grid[i].append('❤️')
              
        # condition for printing stars to right upper
        elif j > m//2 and ((i+j == n//2-3+m//2 and j < 3*m//4) \
                           or (j-i == m//2-n//2+3+m//2 and j >= 3*m//4)):
            print("❤️", end=" ")
            grid[i].append('❤️')
              
        # condition for printing spaces
        else:
            print(" ", end=" ")
            grid[i].append(' ')
    print()
  
# loops for lower part
for i in range(n//2-1, n):
    grid.append([])
    for j in range(m):
          
        # condition for printing stars
        if (i-j == n//2-1) or (i+j == n-1+m//2):
            grid[i].append('❤️')
            print('❤️', end=" ")

        # condition for printing spaces
        else:
            grid[i].append(' ')
            print(' ', end=" ")
              
    print()


# For making heart shape ends here


sr = len(grid)//2
sc = len(grid[0])//2
newColor = '❤️'
change = grid[sr][sc]
height = len(grid)
width = len(grid[0])

startTimer = time.time()
floodFill(grid,sr,sc,newColor)
endTimer = time.time()

# For printing the final heart
for row in grid:
    for i in row:
        print(i if i!='' else ' ',end='')
    print()

print(f"================== DFS PROGRAM FINISHED in %.2f Seconds =================="%(time.time()-startTimer))
