a = int(input())
b=  int(input())
ans = 0
c = []
for i in range(a):
    c.append(int(input()))
for i in range(a):
    d=c[i]
    if d<b:
        ans+=1
    for j in range(i+1,a):
        d=d^c[j]
        if d<b:
            ans+=1
print(ans)