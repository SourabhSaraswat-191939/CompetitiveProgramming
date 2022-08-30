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
        return True
    return False