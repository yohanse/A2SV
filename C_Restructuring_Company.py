class Disjoint:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
    
    def update_rank(self, a, b):
        if self.rank[a] > self.rank[b]:
            self.rank[a] = max(self.rank[a], self.rank[b] + 1)
        else:
            self.rank[b] = max(self.rank[b], self.rank[a] + 1)
    
    def union(self, a, b, c):
        px, py = self.find(a), self.find(b)
        if px != py:
            if self.rank[px] > self.rank[py]:
                self.parent[py] = px   
            else:
                self.parent[px] = py
            
            self.update_rank(px, py)
    
    def find(self, a):
        if a != self.parent[a]:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def is_connected(self, a, b):
        return self.find(a) == self.find(b)
    
n, q = list(map(int, input().split()))

disjoint = Disjoint(n)   
for _ in range(q):
    t, a, b = list(map(int, input().split()))
    if t == 1:
        disjoint.union(a, b)
    elif t == 2:
        for 
