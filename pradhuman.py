result=[0]

def firstMissingPositive(arr, n):
    for i in range(n):
        while (arr[i] >= 1 and arr[i] <= n and arr[i] != arr[arr[i] - 1]):
            temp = arr[i]
            arr[i] = arr[arr[i] - 1]
            arr[temp - 1] = temp
     
    for i in range(n):
        if (arr[i] != i + 1):
            return i + 1
        
    return n + 1

def printSubsequences(arr, index, subarr,n):
	if index == len(arr):
		if len(subarr) != 0:
			result[0]+=firstMissingPositive(subarr,len(subarr))
	
	else:
		printSubsequences(arr, index + 1, subarr,n)
		printSubsequences(arr, index + 1,subarr+[arr[index]],n)
	
	return


n=int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

printSubsequences(arr, 0, [],n)

mod=1e9+7
print(int((result[0]+1)%mod))