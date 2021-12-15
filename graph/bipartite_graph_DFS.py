def bipartiteDFS(node,color):
    for neighbour in graph[node]:
        if color[neighbour]==-1:
            color[neighbour] = not color[node]
            if not bipartiteDFS(neighbour,color):
                return False
        elif color[neighbour]==color[node]:
            return False
    
    return True


        

def isBipartite(graph):
    n=len(graph)
    color = [-1]*n
    for i in range(n):
        if color[i]==-1:
            color[i]=1
            if not bipartiteDFS(i,color):
                return False
    print(color)
    return True

graph = [[3,4,6],[3,6],[3,6],[0,1,2,5],[0,7,8],[3],[0,1,2,7],[4,6],[4],[]]
print(isBipartite(graph))