class Disjoint:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        self.score = [sys.maxsize for i in range(n)]
    
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
        self.score[py] = min(self.score[px], self.score[py], c)
        self.score[px] = min(self.score[px], self.score[py], c)
    
    def find(self, a):
        while a != self.parent[a]:
            a = self.parent[a]
        return a

    def back_score(self, a):
        return self.score[self.find(a)]

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        disjoint = Disjoint(n)
        for a, b, c in roads:
            disjoint.union(a - 1, b - 1, c)
        return disjoint.back_score(n - 1)