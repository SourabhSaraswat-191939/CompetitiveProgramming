# suitable for small dataset or dataset in which some of the elements are not sorted.
#  T.C. -> O(N^2)      S.C. -> O(1)

arr = [64,1,25,12,22,11,14,12]
n = len(arr)
for i in range(n):
    print("check")
    curr=i
    while curr>0 and arr[curr-1]>arr[curr]:
        arr[curr],arr[curr-1] = arr[curr-1],arr[curr]
        curr-=1
    
print(arr)