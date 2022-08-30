day = input()
n = int(input())

# n+=1
d = {"mon":6,"tue":5,"wed":4,"thr":3,"fri":2,"sat":1,"sun":0}
ans = 0
if n>d[day]:
    ans=1 + (n-d[day])//7

print(ans) 



"xuwdbdqik"
[[4,8,0],[4,4,0],[2,4,0],[2,4,0],[6,7,1],[2,2,1],[0,2,1],[8,8,0],[1,3,1]]
