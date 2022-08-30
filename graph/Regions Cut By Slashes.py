class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        # to represent 3 * 3 squares matrix there will be 4 nodes in each row and each columns.
        # So, similarly for n * n matrix there will be (n+1) rows and (n+1) columns, i.e. total of (n+1)**2 number of nodes.
        dots = len(grid)+1
        parent = [i for i in range(dots**2)] 
        rank = [0]*(dots**2)
        global count
        count = 1
        def findParent(x):
            if parent[x]==x:
                return x
            return findParent(parent[x])
        
        def union(x,y):
            global count
            xSet = findParent(x)
            ySet = findParent(y)
            if xSet == ySet:
                count += 1
                return
            
            if rank[xSet]>rank[ySet]:
                parent[ySet] = xSet
            elif rank[xSet]<rank[ySet]:
                parent[xSet] = ySet
            else:
                parent[ySet] = xSet
                rank[xSet] += 1
        
        # to connect all the boundaries of the matrix with nodes.
        for i in range(dots):
            for j in range(dots):
                if i==0 or j==0 or i==dots-1 or j==dots-1:
                    cellNumber = (i*dots)+j    # cellNumber is the numbering of node.
                    if cellNumber!=0:
                        union(0,cellNumber)
        
        for i in range(dots-1):
            ch = grid[i]
            for j in range(dots-1):
                if ch[j]=='/':
                    firstNode = (i*dots)+(j+1)
                    secondNode = ((i+1)*dots)+(j)
                    union(firstNode, secondNode)
                elif ch[j]=='\\':
                    firstNode = (i*dots)+(j)
                    secondNode = ((i+1)*dots)+(j+1)
                    union(firstNode, secondNode)
        
        return count
                
                
        