# The Merge Sort algorithm is a sorting algorithm that is considered as an example of \
# the divide and conquer strategy. So, in this algorithm, the array is initially divided \
# into two equal halves and then they are combined in a sorted manner. We can think of it \
# as a recursive algorithm that continuously splits the array in half until it cannot be \
# further divided. This means that if the array becomes empty or has only one element left,\ 
# the dividing will stop, i.e. it is the base case to stop the recursion. If the array has \
# multiple elements, we split the array into halves and recursively invoke the merge sort \
# on each of the halves. Finally, when both the halves are sorted, the merge operation is \
# applied. Merge operation is the process of taking two smaller sorted arrays and combining \
# them to eventually make a larger one.


#  T.C. -> T(n) = 2T(n/2) + θ(n) = O(nlogn) in all cases (best,avg,worst)   Aux.S.C. -> O(N)

arr = [64,1,25,12,22,11,14,12]
n = len(arr)

def merge(left,mid,right):
    length = min(mid-left,right-mid)
    L = arr[:mid+1]
    R = arr[mid+1:]
    i=j=k=0
    while i<len(L) and j<len(R):
        if L[i]<=R[j]:
            arr[k]=L[i]
            i+=1
        elif L[i]>R[j]:
            arr[k]=R[j]
            j+=1
        k+=1
    while i<len(L):
        arr[k]=L[i]
        i+=1
        k+=1
    while j<len(R):
        arr[k]=R[j]
        j+=1
        k+=1

def mergeSort(left,right):
    if left>=right:
        return
    mid = (left+right)//2
    mergeSort(left,mid)
    mergeSort(mid+1,right)
    merge(left,mid,right)

mergeSort(0,n-1)
print(arr)

