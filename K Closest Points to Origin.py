import heapq
def kClosest(points, k):
    distArr = []
    heap = []
    heapq.heapify(heap)
    for x,y in points:
        dist = x**2 + y**2
        if len(heap)==k:
            print("wokr")
            # print("inside",heap.queue[k-1])
            print(-heap[0][0],dist)
            if -heap[0][0]<= dist:
                print("Chcel")
                continue
            heapq.heappop(heap)
            # print("out",heap.get())

        heapq.heappush(heap,(-dist,x,y))
        print(heap)

    while heap != []:
        w,x,y = heapq.heappop(heap)
        distArr.append([x,y])

    return distArr