from queue import PriorityQueue
import time
from collections import deque

# Using my approach
def findMST1(n,graph):  # using prim's algorithm    Time complexitiy => (N+E) + NLog(N)
    key = [1e9]*n
    parent = [-1]*n
    key[0] = 0
    mst = [False]*n
    parent[0] = 0
    for i in range(n):
        mini = (1e9,1e9)
        for neighbour, wt in graph[i]:
            if wt<mini[1]:
                # if key[neighbour]<=wt:
                #     continue
                mini = (neighbour,wt)
        key[i] = mini[1]
        parent[i] = mini[0]
        # print(i, "=> ", mini)
    print(parent)



# Using brute force approach

def findMST2(n,graph):  # using prim's algorithm    Time complexitiy => (N+E) + N^2
    key = [1e9]*n
    mst = [False]*n
    parent = [-1]*n
    key[0] = 0
    parent[0] = 0
    for i in range(n-1):
        mini = 1e9
        u = None

        for v in range(n):
            if mst[v]==False and key[v]<=mini:
                mini = key[v]
                u = v
        
        mst[u] = True
        for neighbour, wt in graph[u]:
            if mst[neighbour]==False and key[neighbour]>wt:
                parent[neighbour] = u
                key[neighbour] = wt
                
    print(parent)


# Using Min Heap to optimize the brute force approach

def findMST3(n,graph):  # using prim's algorithm  Time complexitiy => (N+E) + NLog(N)
    key = [1e9]*n
    mst = [False]*n
    parent = [-1]*n
    key[0] = 0
    parent[0] = 0
    pq = PriorityQueue()
    pq.put((0,0))
    for i in range(n-1):
        out = pq.get()
        u = out[0]
        mst[u] = True
        for neighbour, wt in graph[u]:
            if mst[neighbour]==False and key[neighbour]>wt:
                pq.put((neighbour, wt))
                parent[neighbour] = u
                key[neighbour] = wt
                
    print(parent)


n = 5
m = 6
graph = {}
print("Enter Graph Values")
for i in range(m):
    a,b, wt = map(int,input().split())
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append((b,wt))
    graph[b].append((a,wt))

# print(graph)
start = time.time()
findMST1(n, graph)
t1 = (time.time()-start)
print("First Time Period %.6f"%(time.time()-start))
start = time.time()
findMST2(n, graph)
t2 = (time.time()-start)
print("Second Time Period %.6f"%(time.time()-start))
start = time.time()
findMST3(n, graph)
t3 = (time.time()-start)
print("Second Time Period %.6f"%(time.time()-start))
print("MST1 wins" if t1<t2 else "MST2 wins")


# 0 1 2
# 1 2 3
# 0 3 6
# 3 1 8
# 1 4 5
# 4 2 7





