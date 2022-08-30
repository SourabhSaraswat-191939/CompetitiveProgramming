class graph:
    def __init__(self,n) -> None:
        self.adj = []
        self.v = n
    
    def addEdge(self,u,v,wt):
        self.adj.append((wt,u,v))

    def findParent(self,x,parent):
        if parent[x] == x:
            return x
        return self.findParent(parent[x],parent)
    
    def union(self,x,y,parent,rank):
        xSet = self.findParent(x,parent)
        ySet = self.findParent(y,parent)

        if xSet==ySet:
            return
        if rank[xSet]<rank[ySet]:
            parent[xSet] = parent[ySet]
        elif rank[xSet]>rank[ySet]:
            parent[ySet] = parent[xSet]
        else:
            parent[ySet] = parent[xSet]
            rank[xSet] += 1
    
    def kruskal(self):
        mst = []
        self.adj.sort()
        parent = [i for i in range(self.v)]
        rank = [0]*self.v
        e = 0
        i=0
        while e<self.v - 1:
            wt,x,y = self.adj[i]
            i+=1
            u = self.findParent(x,parent)
            v = self.findParent(y,parent)

            if u!=v:
                e+=1
                mst.append([x,y,wt])
                self.union(u,v,parent,rank)
            
        minCost = 0
        print ("Edges in the constructed MST")
        for u, v, weight in mst:
            minCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree" , minCost)


g = graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.kruskal()