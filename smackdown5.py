# T = int(input())
# for _ in range(T):
#     s1= input()
#     s2= input()
#     x= input()
#     res = []
    
#     for i in range(len(s1)+1):
#         for j in range(len(s2)+1):
#             res.append(s1[:i]+s2[:j])

#     result = 0
#     for subString in res:
#         if x.find(subString)==-1:
#             pass
#         else:
#             result +=1
        
#     print(result)


hot = ['one','three']
new = ['zero']
new.append(hot)
# hot.append('two')

# print(hot)
# print(new)

for i in new:
    print(i)