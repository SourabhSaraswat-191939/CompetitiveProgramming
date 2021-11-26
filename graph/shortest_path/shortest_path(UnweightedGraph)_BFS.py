from typing import Dict, List
from collections import deque

class Graph:
    def __init__(self) -> None:
        self.gDict =dict()
    def add_edge(self,n1, n2, biDir = True):
        if n1 not in self.gDict:
            self.gDict[n1] = []
        self.gDict[n1].append(n2)
        if biDir:
            if n2 not in self.gDict:
                self.gDict[n2] = []
            self.gDict[n2].append(n1)

    def print(self):
        for key,val in self.gDict.items():
            print(key,"-->",val)

    def shortestPath(self,src):
        dist = [1e7]*len(self.gDict)
        dist[src] = 0
        queue = deque()
        queue.append(src)
        while queue:
            out = queue.popleft()
            for neighbour in self.gDict[out]:
                if dist[neighbour]>dist[out]+1:
                    dist[neighbour] = dist[out]+1
                    queue.append(neighbour)
        
        for i in self.gDict:
            print(i,"=>",dist[i])



g1 = Graph()
g1.add_edge(0,1)
g1.add_edge(0,3)
g1.add_edge(1,2)
g1.add_edge(3,4)
g1.add_edge(4,5)
g1.add_edge(5,6) 
g1.add_edge(2,6)
g1.add_edge(6,7)
g1.add_edge(6,8)
g1.add_edge(7,8)
g1.print()
print("############## Shortest Path ###############")
g1.shortestPath(2)
