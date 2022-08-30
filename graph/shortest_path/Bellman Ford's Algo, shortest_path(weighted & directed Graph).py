import sys
maxVal = sys.maxsize
class Graph:
    def __init__(self,n) -> None:
        self.v = n
        self.adj = []
    def add_edge(self,u,v,w):
        self.adj.append([u,v,w])
        
    def print(self,dist):
        print("Vertex Distance from Source") 
        for i in range(self.v): 
            print("{0}\t\t{1}".format(i, dist[i])) 

    def bellmonFords(self,src):
        shortest_path = [maxVal]*self.v
        
        shortest_path[src] = 0
        
        for _ in range(self.v -1):
            for u,v,w in self.adj:
                if shortest_path[u] + w < shortest_path[v]: 
                        shortest_path[v] = shortest_path[u] + w 

        for u,v,w in self.adj:
                if shortest_path[u] + w < shortest_path[v]: 
                        print("Negative Cycle Detected")

        self.print(shortest_path)                        
            

g = Graph(3)
g.add_edge(0,1,3)
g.add_edge(1,2,-4)
g.add_edge(2,0,-2)
# g.dfs(2)
# print("Connected Components count ->",g.connectedComp())

print("########## Bellmon Ford's Algorithm ###########")
g.bellmonFords(0)
