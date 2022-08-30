# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping \
# the adjacent elements if they are in the wrong order. This algorithm is not suitable \
# for large data sets as its average and worst-case time complexity is quite high.

# in this we are fixing 1 element after each iteration, i.e. the last element of array.
# It is optimized by stopping the algorithm if the inner loop didn’t cause any swap. 

#  T.C. -> O(N^2)      S.C. -> O(1)

arr = [64,1,25,12,22,11,14,12]
n = len(arr)

swapped=False
for i in range(n):
    curr=0
    for j in range(1,n-i):
        if arr[j]<arr[curr]:
            arr[j],arr[curr]=arr[curr],arr[j]
            swapped=True
        curr+=1

    if swapped == False: 
        break

print(arr)