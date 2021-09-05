# Enter your code here. Read input from STDIN. Print output to STDOUT
heap = [None]
def insert(val):
    n = len(heap) 
    heap.append(val)
    i=n
    while i>1:
        parent = int(i/2)
        # print(heap)
        # print("i=> ",i,"parent=> ",parent)
        if heap[parent]>heap[i]:
            temp = heap[parent]
            heap[parent] = heap[i]
            heap[i] = temp
            i = parent
        else:
            return

def delete(val):
    heap[1] = heap.pop()
    n = len(heap) - 1
    i=1
    while i<n:
        left = heap[2*i]
        right = heap[(2*i)+1]
        smaller = (2*i) if left<right else (2*i)+1
        if heap[i]>heap[smaller]:
            temp = heap[smaller]
            heap[smaller] = heap[i]
            heap[i] = temp
            i = smaller
        else:
            return

Q = int(input())
for i in range(Q):
    op = input().split()
    if op[0] == '1':
        insert(op[1])
    if op[0] == '2':
        delete(op[1])
    if op[0] == '3':
        print(heap[1])