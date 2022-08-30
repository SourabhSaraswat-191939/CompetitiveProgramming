def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

x,y = map(int,input("Enter 2 numbers to find GCD :- ").split())
print(gcd(x,y))