# Sub version of problem 33 on leetcode

from math import ceil
arr = [11,12,14,18,2,3,4,5]
n=len(arr)
def binary_search(start,end):
    while start<=end:
        mid = ceil((start+end)/2)
        if arr[mid]<=arr[(mid+n-1)%n] and arr[mid]<=arr[(mid+1)%n]:
            return mid
        
        if arr[start]<=arr[mid]:
            start= mid+1
        elif arr[mid]<=arr[end]:
            end= mid-1
            
        binary_search(start,end)

print("Index of minimum element -> ",binary_search(0,n-1))