import sys
maxVal = sys.maxsize
class Graph:
    def __init__(self,n) -> None:
        self.v = n
        self.adj = [None]*(n+1)
    def add_edge(self,n1,n2,weight,biDir = True):
        if self.adj[n1] is None:
            self.adj[n1] = []
        self.adj[n1].append([n2,weight])
        if biDir:
            if self.adj[n2] is None:
                self.adj[n2] = []
            self.adj[n2].append([n1,weight])    
    def print(self):
        print(self.adj)

    def shortestDistance(self,src,dest):
        shortest_path = [maxVal]*self.v
        previous_nodes = {}
        shortest_path[src] = 0
        heap = set()
        heap.add((src,0))
        while heap:
            out, weight = heap.pop()
            for neighbour, n_weight in self.adj[out]:
                if shortest_path[neighbour]>weight+n_weight:
                    shortest_path[neighbour] = weight+n_weight
                    heap.add((neighbour,shortest_path[neighbour]))
                    previous_nodes[neighbour] = out
        print("################## Shortest Path Distance ####################")
        print(shortest_path)
        print("################## Path with Nodes ####################") 
        while dest!=src:
            print(dest,end='<-')
            dest = previous_nodes[dest]
        print(src)
        # print(previous_nodes)



        # shortest_path = {}
        # previous_nodes = {}
        # unvisited_nodes = [x for x in range(self.v)]
        # for node in unvisited_nodes:
        #     shortest_path[node] = maxVal
        # shortest_path[src] = 0
        
        # while unvisited_nodes:
            
            

g = Graph(7)
g.add_edge(0,1,2)
g.add_edge(1,3,5)
g.add_edge(0,2,1)
g.add_edge(2,3,8)
g.add_edge(3,5,15)
g.add_edge(3,4,10)
g.add_edge(4,5,6)
g.add_edge(4,6,2)
g.add_edge(6,5,6)
# g.dfs(2)
# print("Connected Components count ->",g.connectedComp())
g.print()

print("########## Dijkistra's Algorithm ###########")
g.shortestDistance(0,4)
