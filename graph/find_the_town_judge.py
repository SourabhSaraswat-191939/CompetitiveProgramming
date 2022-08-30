class Graph:
    def __init__(self,n) -> None:
        self.adj = dict()
        self.v = n
    def insert(self,v1,v2):
        if v1 not in self.adj:
            self.adj[v1] = set()
        self.adj[v1].add(v2)
        if v2 not in self.adj:
            self.adj[v2] = set()
            
    def judge(self):
        for key in self.adj:
            if len(self.adj[key])==0:
                return key
        return -1
    
    def findResult(self):
        judge = self.judge()
        if judge==-1:
            return -1
        for key in self.adj:
            if judge==key:
                continue
            if judge not in self.adj[key]:
                return -1
        return judge
