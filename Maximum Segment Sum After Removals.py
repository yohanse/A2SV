class Disjoint:
    def __init__(self, n):
        self.parent = [-1 for i in range(n)]
        self.rank = [0 for i in range(n)]
        self.score = [0 for i in range(n)]
    
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
                self.score[px] += self.score[py]
            else:
                self.parent[px] = py
                self.score[py] += self.score[px]
            
            self.update_rank(px, py)
    
    def find(self, a):
        while a != self.parent[a]:
            a = self.parent[a]
        return a
    
    def isConnected(self, a, b):
        return self.find(a) == self.find(b)
    
    def value(self, a):
        return self.parent[a]
    
    def setValue(self, a):
        self.parent[a] = a
    
    def setScore(self, a, b):
        self.score[self.find(a)] += b
        return self.score[self.find(a)]


class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        N = len(nums)
        ans = 0
        result = [0 for i in range(N)]
        disjoint = Disjoint(N)
        for i in range(N - 1, -1, -1):
            left, right = removeQueries[i] - 1, removeQueries[i] + 1
            disjoint.setValue(left + 1)

            if left > -1 and disjoint.value(left) != -1:
                disjoint.union(left, left + 1)

            if right < N and disjoint.value(right) != -1:
                disjoint.union(right, right - 1)

            result[i] = ans
            ans = max(ans, disjoint.setScore(left + 1, nums[left + 1]))
            
        return result


        