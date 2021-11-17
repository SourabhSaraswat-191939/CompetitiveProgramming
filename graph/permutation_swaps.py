class Graph:
    def __init__(self) -> None:
        self.arr = dict()
    
    def add_edge(self,n1,n2):
        if n1 not in self.arr:
            self.arr[n1] = []
        self.arr[n1].append(n2)

        if n2 not in self.arr:
            self.arr[n2] = []
        self.arr[n2].append(n1)

    def printAll(self):
        print(self.arr)


    def dfs(self,src,visited=dict()):
        if src not in self.arr:
            return
        visited[src] = True
        for neighbour in self.adj[src]:
            if neighbour not in visited:
                self.dfs(neighbour,visited)

    def connectedComponents(self,P,Q):
        visited = dict()
        
        for i in range(len(P)):
            if P[i]==Q[i]:
                continue
            if P[i] not in visited:
                self.dfs(i,visited)
                
            if Q[i] not in visited:
                return False
        return True
    # def dfs(self,src,visited=dict()):
    #     if src not in self.arr:
    #         return
    #     visited[src] = True
        
    #     for neighbour in self.arr[src]:
    #         if neighbour not in visited:
    #             self.dfs(neighbour,visited)

    # def connectedComponents(self,P,Q):
    #     for i in range(len(P)):
    #         visited= dict()
    #         if P[i]==Q[i]:
    #             continue
    #         if P[i] not in visited:
    #             self.dfs(P[i],visited)
    #         print("Visited",visited)
    #         print("-----------")
    #         if Q[i] not in visited:
    #             return False
    #     return True

T = int(input())
for _ in range(T):
    g = Graph()
    N,M = map(int,input().split())
    P = list(map(int,input().split()))
    Q = list(map(int,input().split()))
    for _ in range(M):
        n1,n2 = map(int,input().split())
        g.add_edge(n1,n2)
    # g.printAll()

    if g.connectedComponents(P,Q):
        print("YES")
    else:
        print("NO")
    # result = 1
    # for i in range(len(P)):
    #     if P[i]==Q[i]:
    #         continue
    #     if g.dfs(P[i],Q[i]):
    #         continue
    #     else:
    #         result = 0
    #         print("\nNo for -> ",str(P[i]),"\n")
    #         exit

    # if result:
    #     print("YES")
    # else:
    #     print("NO")