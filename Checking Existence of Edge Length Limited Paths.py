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
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:

        disjoint = Disjoint(n)
        edgeList.sort(key = lambda x: x[2])
        indices = [i for i in range(len(queries))]
        indices.sort(key = lambda x: queries[x][2])

        curr_edge = 0
        result = [False for i in range(len(queries))]
        for i in indices:
            while curr_edge < len(edgeList) and edgeList[curr_edge][2] < queries[i][2]:
                disjoint.union(edgeList[curr_edge][0], edgeList[curr_edge][1])
                curr_edge += 1
            result[i] = disjoint.isConnected(queries[i][0], queries[i][1])
        return result
            
        
            










