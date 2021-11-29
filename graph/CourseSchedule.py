# def canFinish(numCourses, prerequisites):
#     adjList = {}
#     for course in prerequisites:
#         if course[0] not in adjList:
#             adjList[course[0]] = []
#         adjList[course[0]].append(course[1])
    
#     print(adjList)
#     visited = set()
#     def dfs(src):
#         if src not in adjList:
#             return True
#         if src in adjList[src]:
#             print("First")
#             return False
#         visited.add(src)
        
#         print("Looping for", src)
#         for neighbour in adjList[src]:
#             # print(neighbour, visited)
#             if neighbour in visited:
#                 print("Second", neighbour)
#                 return False          
#             return dfs(neighbour)
#         visited.remove(src)
#         adjList[course[0]] = []
#         return True

#     for course in range(numC):
#         # visited.add(course[0])
#         if not dfs(course):
#             return False
        
#     return True

    
#     # return    

# prereq = [[1,4],[2,4],[3,1],[3,2]]
# numC = 5
# print(canFinish(numC, prereq))







##    With topological sort    ##
from collections import deque
def canFinish(numCourses, prerequisites):
    adjList = {}
    inDegree = [0]*numCourses
    for course in prerequisites:
        inDegree[course[1]] += 1
        if course[0] not in adjList:
            adjList[course[0]] = []
        adjList[course[0]].append(course[1])

    topo = []
    queue = deque()
    for i in range(numCourses):
        if inDegree[i]==0: queue.append(i)
    while queue:
        out = queue.popleft()
        topo.append(out)
        if out in adjList:
            for neighbour in adjList[out]:
                inDegree[neighbour] -= 1
                if not inDegree[neighbour]:
                    queue.append(neighbour)
    if len(topo)==numCourses:
        topo.reverse()
        return topo
    return []
    

prereq = [[1,4],[2,4],[3,1],[3,2]]
numC = 5
print(canFinish(numC, prereq))