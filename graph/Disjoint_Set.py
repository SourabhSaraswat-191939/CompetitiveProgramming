class DisjSet:
    def __init__(self,n) -> None:
        self.rank = [0]*n
        self.parent = [i for i in range(n)]

    def findParent(self, x):
        if self.parent[x]==x:
            return x
        
        return self.findParent(self.parent[x])

    def Union(self,x,y):
        xset = self.findParent(x)
        yset = self.findParent(y)
        if xset==yset:
            return
           
        if self.rank[xset]<self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset]>self.rank[yset]:
            self.parent[yset] = xset    
        else:
            self.parent[yset] = xset    
            self.rank[xset] += 1

obj = DisjSet(5)
obj.Union(0, 2)
obj.Union(4, 2)
obj.Union(3, 1)
if obj.findParent(4) == obj.findParent(0):
    print('Yes')
else:
    print('No')
if obj.findParent(1) == obj.findParent(0):
    print('Yes')
else:
    print('No')
  