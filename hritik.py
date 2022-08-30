from collections import deque

def Pairs(N,A):
    result=[]
    l=0
    r=1
    count=0
    andRes = A[l]
    while l<=r:
        # print(l,r)
        if A[l]>A[r] or andRes<=0:
            l+=1
            andRes=A[l]
            continue
        else:
            # print("check")
            count+=1
            r+=1

        if r>=len(A):
            l=l+1
            r=l+1
        # print("yes",l,r,len(A))
        if l>=len(A) or r>=len(A):
            # print("work")
            break

    return count

    # for i in range(len(A)):
    #     andRes = A[i]
    #     for j in range(i+1,len(A)):
    #         if A[i]>A[j]:
    #             continue
    #         elif andRes & A[j]<=0:
    #             break
    #         else:
    #             result.append((i+1,j+1))
    # mod=1e9+7
    # return int(len(result)%mod)


print(Pairs(5,[6,6,1,3,4]))
# print(Pairs(5,[2,2,2,5,3]))
# print(Pairs(5,[2,6,3,3,3]))