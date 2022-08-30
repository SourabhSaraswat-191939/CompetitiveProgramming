def solve (N, A):
    # Write your code here
    dicti = {}
    X = []
    Y = []
    for i in range(N):
        dicti[A[i]] = i
        innerDicti = {}
        for j in range(i+1,N):
            if (A[j] not in dicti):
                innerDicti[A[j]] = j
        X.append(len(innerDicti))
    
    dicti = {}
    for m in range(N-1,-1,-1):
        dicti[A[m]] = m
        print(dicti)
        innerDicti = {}
        for n in range(m-1,-1,-1):
            if (A[n] not in dicti):
                innerDicti[A[n]] = n
        Y.append(len(innerDicti))

    Y.reverse()   
    result = [] 
    for i in range(N):
        result.append(abs(X[i]-Y[i]))

    return result






# solve(5, [7,7,3,2,3])
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    out_ = solve(N, A)
    print (' '.join(map(str, out_)))

