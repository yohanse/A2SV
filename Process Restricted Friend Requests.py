class Disjoint:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
    
    def update_rank(self, a, b):
        if self.rank[a] > self.rank[b]:
            self.rank[a] = max(self.rank[a], self.rank[b] + 1)
        else:
            self.rank[b] = max(self.rank[b], self.rank[a] + 1)
    
    def union(self, a, b):
        px, py = self.find(a), self.find(b)
        if px != py:
            if self.rank[px] > self.rank[py]:
                self.parent[py] = px
            else:
                self.parent[px] = py
            
            self.update_rank(px, py)
    
    def find(self, a):
        while a != self.parent[a]:
            a = self.parent[a]
        return a
    
    def isConnected(self, a, b):
        return self.find(a) == self.find(b)



class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        disjoint = Disjoint(n)
        result = []
        for a, b in requests:
            temp = disjoint.parent.copy()
            disjoint.union(a, b)
            for i, j in restrictions:
                if disjoint.isConnected(i, j):
                    disjoint.parent = temp
                    result.append(False)
                    break
            else:
                result.append(True)
        return result


