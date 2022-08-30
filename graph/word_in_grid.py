# IMPORTANT as per interview perspective.

def recurse(grid, word, word_index, row, col):
    if word_index>=len(word):
        return True
    if row<0 or col<0 or row>=len(grid) or col>=len(grid[0]):
        return False
    if grid[row][col]!=word[word_index]:
        return False

    grid[row][col] = '$'
    retVal = True
    rows = [-1,1,0,0]
    cols = [0,0,-1,1]
    for i in range(4):
        retVal = recurse(grid, word, word_index+1, row+rows[i], col+cols[i])
        if retVal: 
            break 
    grid[row][col] = word[word_index]
    return retVal

def find(grid, word):
    # first find cells having first letter of the word. So that we can apply dfs.
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==word[0]:
                if recurse(grid,word,0,i,j):
                    return True
    return False

m = int(input("Enter Rows count -> "))
n = int(input("Enter Columns count -> "))
grid = []
print("START entering grid")
word = input("Enter Word -> ")
for i in range(m):
    grid.append([])
    for j in range(n):
        grid[i].append(input())

print(grid)

if find(grid,word):
    print("Word found")
else:
    print("Word not found")

