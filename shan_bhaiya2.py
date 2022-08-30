def kCores(graph,k):
    if graph==None:
        return None
    degreeL = [0]*len(graph)
    rem = set()
    def findDegree(G,ver, n):
        degree = 0
        for i in range(n):
            if G[ver][i] == 1:
                degree += 1
        if G[ver][ver] == 1: 
            degree += 1
        degreeL[ver] = degree
        if degree<k:
            rem.add(G[ver][i])
            for i in range(n):
                if G[ver][i] == 1:
                    G[ver][i]=0
                    G[i][ver]=0
                    findDegree(G,i,n)
            if G[ver][ver] == 1: 
                G[ver][ver] = 1
            degreeL[ver] =0
        
        return degree
    
    for i in range(len(graph)):
        if i not in rem:
            findDegree(graph,i,len(graph))
    
    return graph

# graph = [[0,1,1,0,0,0,0],[1,0,1,0,0,1,0],[1,1,0,1,1,1,1],[0,0,1,0,1,0,1],[0,0,1,1,0,0,1],[0,1,1,0,0,0,0],[0,0,1,1,1,0,0]]
graph = [[0,1,0,1,0,0],[1,0,1,1,0,1],[0,1,0,1,1,1],[1,1,1,0,0,1],[0,0,1,0,0,1],[0,1,1,1,1,0]]

new = kCores(graph,3)

for val in new:
    print(val)