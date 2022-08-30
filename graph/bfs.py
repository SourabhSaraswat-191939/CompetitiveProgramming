from collections import deque
class Graph:
    def __init__(self,n) -> None:
        self.v = n
        self.adj = [None]*(n+1)
    def add_edge(self,n1,n2,biDir = True):
        if self.adj[n1] is None:
            self.adj[n1] = []
        self.adj[n1].append(n2)
        if biDir:
            if self.adj[n2] is None:
                self.adj[n2] = []
            self.adj[n2].append(n1)    
    def print(self):
        print(self.adj)
    def dfsHelper(self, src, visited):
        visited[src] = True
        print(src)
        for neighbour in self.adj[src]:
            if neighbour not in visited:
                self.dfsHelper(neighbour,visited)

    def dfs(self, src):
        visited = dict()
        self.dfsHelper(src, visited)
    
    def bfsHelper(self, src,visited):
        queue = deque()
        queue.append(src)
        visited[src] = True
        while queue:
            out = queue.popleft()
            print(out,end=" ")
            if self.adj[out] is None:
                break
            for neighbour in self.adj[out]:
                if not visited[neighbour]:
                    queue.append(neighbour)
                    visited[neighbour] = True

    def bfs(self):
        visited = [False]*(self.v+1)
        for i in range(self.v):            
            print("Connected Components")
            if visited[i]==False:
                self.bfsHelper(i,visited)
        del visited

g = Graph(7)
# g.add_edge(0,1)
# g.add_edge(0,3)
# g.add_edge(1,4)
# g.add_edge(1,2)
# g.add_edge(2,5)
# g.add_edge(2,6)
# g.add_edge(3,4)
# g.add_edge(5,6)
g.add_edge(1,1)
g.add_edge(2,5)
g.add_edge(2,4)
g.add_edge(3,1)
g.add_edge(2,2)
# g.dfs(2)
# print("Connected Components count ->",g.connectedComp())
# g.print()
g.bfs()