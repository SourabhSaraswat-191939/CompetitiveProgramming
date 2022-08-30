from typing import Dict, List

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


g1 = Graph()
g1.add_edge(2,4)
g1.add_edge(4,3)
g1.add_edge(2,3)
g1.add_edge(3,1)

g1.print()