class Graph:
    def __init__(self,n) -> None:
        self.adj = dict()
        self.v = n
    
    def insert(self, v1,v2, bidir =True):
        if v1 not in self.adj:
            self.adj[v1] = []
        self.adj[v1].append(v2)
        if bidir:
            if v2 not in self.adj:
                self.adj[v2] = []
            self.adj[v2].append(v1)
    
    def dfs(self,src,visited=dict()):
        visited[src] = True
        print(src)
        for neighbour in self.adj[src]:
            if neighbour not in visited:
                self.dfs(neighbour,visited)

    def connectedComp(self):
        visited = dict()
        result = 0
        for i in range(1,self.v+1):
            if i not in visited:
                self.dfs(i,visited)
                result +=1
            print("Visited",visited)
            print("-----------")
        return result

g = Graph(6)
g.insert(2,3)
g.insert(4,3)
g.insert(6,1)
g.insert(5,5)
g.insert(1,6)
g.insert(2,4)
# g.dfs(2)
print("Connected Component Count -->",g.connectedComp())
# g.traverse()
