from typing import Dict, List
from collections import deque

class Graph:
    def __init__(self) -> None:
        self.gDict =dict()
    def add_edge(self,n1, n2, biDir = False):
        if n1 not in self.gDict:
            self.gDict[n1] = []
        self.gDict[n1].append(n2)
        if n2 not in self.gDict:
            self.gDict[n2] = []

    def print(self):
        for key,val in self.gDict.items():
            print(key,"-->",val)

    def topologicalSortUtil(self,src,visited,stack):
        visited[src]=1
        for neighbour in self.gDict[src]:
            if not visited[neighbour]:
                self.topologicalSortUtil(neighbour,visited,stack)
        stack.append(src)

    def topologicalSort(self):
        stack = []
        n = len(self.gDict)
        visited = [0]*(n)
        for i in range(n):
            if not visited[i]:
                self.topologicalSortUtil(i,visited,stack)

        print(stack[::-1])





g1 = Graph()
g1.add_edge(5,0)
g1.add_edge(4,0)
g1.add_edge(5,2)
g1.add_edge(2,3)
g1.add_edge(3,1)
g1.add_edge(4,1) 

g1.print()
print("############## Topological Sort ###############")
g1.topologicalSort()
