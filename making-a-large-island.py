class Disjoint:
    def __init__(self, n):
        self.size = [1 for i in range(n)]
        self.rank = [1 for i in range(n)]
        self.pare = [i for i in range(n)]
    

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)

        if pa != pb:
            if self.rank[pa] == self.rank[pb]:
                self.rank[pa] += 1
            
            if self.rank[pa] > self.rank[pb]:
                self.pare[pb] = pa
                self.size[pa] += self.size[pb]
            else:
                self.pare[pa] = pb
                self.size[pb] += self.size[pa]
    
    def find(self, a):
        b = a
        while a != self.pare[a]:
            a = self.pare[a]
        
        while b != self.pare[b]:
            temp = self.pare[b]
            self.pare[b] = a
            b = temp
            
        return a
    
    def number(self, a):
        return self.size[self.find(a)]




class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        disjoint = Disjoint(n * n)

        for i in range(n):
            for j in range(n):
                if i - 1 > -1 and grid[i][j] and grid[i - 1][j]:
                    disjoint.union(i * n + j, (i - 1) * n + j)

                if j - 1 > -1 and grid[i][j] and grid[i][j - 1]:
                    disjoint.union(i * n + j, i * n + j - 1)

        ans = max(disjoint.size)
        for i in range(n):
            for j in range(n):
                if not grid[i][j]:
                    visite, count = set(), 0
                    for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                        x, y = i + dx, j + dy
                        if -1 < x < n and -1 < y < n and grid[x][y] == 1 and disjoint.find(x * n + y) not in visite:
                            visite.add(disjoint.find(x * n + y))
                            count += disjoint.number(x * n + y)
                    ans = max(ans, count + 1)
        return ans