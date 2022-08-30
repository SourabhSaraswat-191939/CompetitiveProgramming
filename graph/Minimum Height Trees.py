n=4
edges = [[1,0],[1,2],[1,3]]
parent = [i for i in range(n)]
rank = [0]*n
def findParent(x):
    if parent[x]==x:
        return x
    return parent[x]

def union(x,y):
    xSet = findParent(x)
    ySet = findParent(y)
    if xSet == ySet:
        return
    if xSet == 1:
        self.parent[yset] = xset    