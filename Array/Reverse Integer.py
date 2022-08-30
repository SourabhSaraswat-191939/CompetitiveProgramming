def reverse(x: int) -> int:
    result= 0
    flag = True if x>=0 else False
    x=abs(x)
    while x!=0:
            result= result*10 + x%10
            x=x//10
    return result if flag else -result

print(reverse(-123))


