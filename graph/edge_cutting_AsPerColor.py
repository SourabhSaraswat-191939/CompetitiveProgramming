from graph_creation import Graph
n = int(input())
g = Graph(n)
countRed = 0
countBlue = 0
ans = 0
colors = []
def dfs(src, parent=-1):    # it will return the count of red and blue
    red = int(colors[src]=='R')
    blue = int(colors[src]=='B')
    for neighbour in g.adj:
        if neighbour != parent:
            result = dfs(neighbour, parent)
            global ans
            ans += int(result['red']==countRed and result['blue']==0)
            ans += int(result['red']==0 and result['blue']==countBlue)
            red += result['red']
            blue +=result['blue']

for i in range(n-1):
    color = input()
    colors[i] = color
    if color=='R':
        countRed +=1
    if color=='B':
        countBlue +=1

for j in range(n-1):
    u = int(input())
    v = int(input())
    g.insert(u-1,v-1)
    g.insert(v-1,u-1)



