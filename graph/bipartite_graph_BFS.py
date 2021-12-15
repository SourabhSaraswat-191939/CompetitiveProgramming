from collections import deque
def bipartiteBFS(node,color):
    color[node] = 1
    queue = deque()
    queue.append(node)
    while queue:
        out = queue.popleft()
        for neighbour in graph[out]:
            if color[neighbour]==-1:
                color[neighbour] = not color[out]
                queue.append(neighbour)
            elif color[neighbour]==color[out]:
                return False
    
    return True


        

def isBipartite(graph):
    n=len(graph)
    color = [-1]*n
    for i in range(n):
        if color[i]==-1:
            if not bipartiteBFS(i,color):
                return False
    print(color)
    return True

graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
print(isBipartite(graph))