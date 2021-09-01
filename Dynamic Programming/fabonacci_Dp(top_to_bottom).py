Dp_arr = [-1]*50
def fib(n):
    if n==0 or n==1:
        Dp_arr[n] = n
        return n
    nthTerm = Dp_arr[n]
    if nthTerm!=-1:
        return nthTerm
    ans = fib(n-1) + fib(n-2)
    Dp_arr[n] = ans
    return ans

for i in range(50):
    print(fib(i))

print(Dp_arr)