# Problem 33 on leetcode

from math import ceil
arr = [11,12,14,18,2,3,4,5,9]
target = 3
n=len(arr)

def binary_search_for_min_index(start,end):
    while start<=end:
        mid = ceil((start+end)/2)
        if arr[mid]<=arr[(mid+n-1)%n] and arr[mid]<=arr[(mid+1)%n]:
            return mid
        
        if arr[start]<=arr[mid]:
            start= mid+1
        elif arr[mid]<=arr[end]:
            end= mid-1
            
        binary_search_for_min_index(start,end)

mini = binary_search_for_min_index(0,n-1)

def binary_search_for_target(start,end):
    if start<=end:
        mid = ceil((start+end)/2)
        if arr[mid]==target:
            return mid
        
        if target>arr[mid]:
            start= mid+1
        elif target<arr[end]:
            end= mid-1
            
        return binary_search_for_target(start,end)
    
    else:
        return -1

result = binary_search_for_target(0,mini-1)
if result>0:
    print("Element is at index -> ",result)

else:
    result = binary_search_for_target(mini,n-1)
    print("Element is at index -> ",result)
