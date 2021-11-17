class Graph:
    def __init__(self,n) -> None:
        self.adj = dict()
        self.v = n
        
    def printAll(self):
        print(self.adj)

    def insert(self,v1,v2):
        if v1 not in self.adj:
            self.adj[v1] = []
        self.adj[v1].append(v2)
        if v2 not in self.adj:
            self.adj[v2] = []
        self.adj[v2].append(v1)

    def dfs(self, start,visited=dict()):
        if start not in self.adj:
            return False
        visited[start] = True
        for neighbour in self.adj[start]:
            if neighbour not in visited:
                print(neighbour)
                self.dfs(neighbour,visited)



n = 10
edges = [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]]
start = 5
end = 9

g = Graph(n)
for pair in edges:
    g.insert(pair[0],pair[1])

g.printAll()
visited=dict()
g.dfs(start,visited)
    
if end in visited:
    print("true")
else:
    print("false")