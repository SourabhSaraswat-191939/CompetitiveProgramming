T = int(input())

for _ in range(T):
    n = int(input())
    t1, t2, t3 = map(int,input().split())
    a, b, c = map(int,input().split())
    A = []
    ques = [t1,t2,t3]
    for _ in range(3):
        A.append(list(map(int,input().strip().split())))
    # for typ in range(3):
    #     for method in range(3):
    #         while
    highest = 1000000001
    result = 0
    for t in range(len(ques)):
        while ques[t]!=0:
            ind = A[t].index(min(A[t]))
            if ind==0:
                if a!=0:
                    if ques[t]-a>=0:
                        result += a*A[t][0]
                        ques[t]-=a
                        a=0
                    else:
                        result += ques[t]*A[t][0]
                        a-=ques[t]
                        ques[t]=0
                else:
                    A[t][ind] = highest

            if ind==1:
                if b!=0:
                    if ques[t]-b>=0:
                        result += b*A[t][1]
                        ques[t]-=b
                        b=0
                    else:
                        result += ques[t]*A[t][1]
                        b-=ques[t]
                        ques[t]=0
                else:
                    A[t][ind] = highest

            if ind==2:
                if c!=0:
                    if ques[t]-c>=0:
                        result += c*A[t][1]
                        ques[t]-=c
                        c=0
                    else:
                        result += ques[t]*A[t][1]
                        c-=ques[t]
                        ques[t]=0
                else:
                    A[t][ind] = highest


    print(result)


# print(1e3)