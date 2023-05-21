class Disjoint:
    def __init__(self, points):
        self.parent = {(i, j):(i, j) for i, j in points}
        self.rank = {(i, j):0 for i, j in points}

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1

            if self.rank[a] > self.rank[b]:
                self.parent[b] = a
            else:
                self.parent[a] = b   
            
    def find(self, a):
        z = a
        while a != self.parent[a]:
            a = self.parent[a]

        while z != self.parent[z]:
            z = self.parent[z]
            self.parent[z] = a
            
        return a
        
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for w in range(n):
            i, j = points[w]
            for e in range(w + 1, n):
                x, y = points[e]
                edges.append([abs(i - x) + abs(y - j), i, j, x, y])

        edges.sort()
        disjoint = Disjoint(points)
        ans = 0
        for m, i, j, x, y in edges:
            if disjoint.find((i, j)) != disjoint.find((x, y)):
                disjoint.union((i, j), (x, y))
                ans += m
        return ans