# For question statement and solution -> https://www.geeksforgeeks.org/minimum-number-increment-operations-make-array-elements-equal/


# def countMoves(numbers):
#     count = 0
#     run = True
#     n = len(numbers)
#     while run:
#         dicti = {}
#         for j in range(n):
#             if len(dicti)>2:
#                 break
            
#             if numbers[j] in dicti:
#                 dicti[numbers[j]] +=1
#             else:
#                 dicti[numbers[j]] = 1

#         if len(dicti)<=2:
#             for key,val in dicti.items():
#                 if val==1:
#                     count +=1
#                     run = False
#                     break

#         if run == False or len(dicti)==1:
#             break    
#         Maxindex = numbers.index(max(numbers))
#         for k in range(n):
#             if k == Maxindex:
#                 continue
#             numbers[k] += 1
#         count+=1      
#     print(dicti)
#     return count




# s = int(input())
# numbe = []
# for i in range(s):
#     numbe.append(int(input()))

# print(countMoves(numbe))







# For GFG

# Python 3 for finding minimum
# operation required

# function for finding min
# operation
def minOp (arr, n) :
	
	# find array sum
	sm = sum(arr)

	# find the smallest element from
	# array
	small = min(arr)

	# calculate min operation required
	minOperation = sm - (n * small)

	# return result
	return minOperation
	
# Driver function
arr = [3,4,6,6,3]
n = len(arr)
print( "Minimum Operation = ", minOp (arr, n))

# This code is contributed by Shubham Singh
