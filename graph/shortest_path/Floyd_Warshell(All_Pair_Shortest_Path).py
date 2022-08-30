# Time Complexity -> O(N^3)

INF = 1e7

def floydWarshall(V,graph):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
    return graph
def printShortestPathMatrix(V,graph):
    print("This matrix shows the shortest distances between every pair of vertices.")
    for i in range(V):
        for j in range(V):
            if(graph[i][j] == INF):
                print("%8s" % ("INF"),end="")
            else:
                print("%8d" % (graph[i][j]),end="")
            if j == V-1:
                print("")

n = 4
graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0,   1],
         [INF, INF, INF, 0]
         ]
# Print the solution
printShortestPathMatrix(n,floydWarshall(n,graph))