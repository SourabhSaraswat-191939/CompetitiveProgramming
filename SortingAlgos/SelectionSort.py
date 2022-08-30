#  T.C. -> O(N^2)      S.C. -> O(1)

arr = [64,1,25,12,22,11,14,12]
n= len(arr)
for i in range(n):
    mini = arr[i]
    replaceIndex = i
    for j in range(i+1,n):
        if mini>arr[j]:
            replaceIndex = j
            mini = arr[j]
    arr[i],arr[replaceIndex] = arr[replaceIndex],arr[i]

print(arr)
