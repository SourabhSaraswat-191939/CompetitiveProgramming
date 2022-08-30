# from collections import deque
# q = deque()
# sum={}
# q.append([3,1])
# print(q.popleft()[0])   
# # while q:
# #     out = q.popleft()
# #     if out.left is not None:
# #         q.append(out.left)
# #     if out.right is not None:
# #         q.append(out.right)

level=1
sum = {1:989,2:10250}
maximal = 989
for key in sum:
    print("key",sum[key],"maximal",maximal)
    if sum[key]>maximal:
        level = key
print(level)