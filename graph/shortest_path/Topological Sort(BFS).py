from typing import Dict, List
from collections import deque

class Graph:
    def __init__(self,n) -> None:
        self.adj =dict()
        self.inDegree = [0]*n
        self.v = n
    def add_edge(self,n1, n2, biDir = False):
        if n1 not in self.adj:
            self.adj[n1] = []
        self.adj[n1].append(n2)
        if n2 not in self.adj:
            self.adj[n2] = []
        self.inDegree[n2] += 1

    def print(self):
        for key,val in self.adj.items():
            print(key,"-->",val)

    def topologicalSortUtil(self,src,visited,stack):
        visited[src]=1
        for neighbour in self.adj[src]:
            if not visited[neighbour]:
                self.topologicalSortUtil(neighbour,visited,stack)
        stack.append(src)

    def topologicalSort_BFS(self):
        print(self.inDegree)
        result = []
        queue = deque()
        for i in range(self.v):
            if self.inDegree[i]==0: queue.append(i)
        
        while queue:
            out = queue.popleft()
            result.append(out)
            for neighbour in self.adj[out]:
                self.inDegree[neighbour] -= 1
                if not self.inDegree[neighbour]:
                    queue.append(neighbour)
        
        print(self.inDegree)
        print(result)
                    




g1 = Graph(6)
g1.add_edge(5,0)
g1.add_edge(3,5)
g1.add_edge(4,0)
g1.add_edge(5,2)
g1.add_edge(2,3)
g1.add_edge(3,1)
g1.add_edge(4,1) 

g1.print()
print("############## Topological Sort ###############")
g1.topologicalSort_BFS()
