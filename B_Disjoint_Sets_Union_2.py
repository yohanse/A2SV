import sys
class Disjoint:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        self.max = [i for i in range(n)]
        self.min = [i for i in range(n)]
        self.sum = [1 for i in range(n)]
        
    def union(self, a, b):
        px, py = self.find(a), self.find(b)
        if px != py:
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1

            if self.rank[px] > self.rank[py]:
                self.parent[py] = px
                self.max[px] = max(self.max[px], self.max[py])
                self.min[px] = min(self.min[px], self.min[py])
                self.sum[px] += self.sum[py]
            else:
                self.parent[px] = py
                self.max[py] = max(self.max[px], self.max[py])
                self.min[py] = min(self.min[px], self.min[py])
                self.sum[py] += self.sum[px]

    def find(self, a):
        if a != self.parent[a]:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def get_min(self, a):
        return self.min[self.find(a)] + 1
    
    def get_max(self, a):
        return self.max[self.find(a)] + 1
    
    def get_ele(self, a):
        return self.sum[self.find(a)]

n, m = list(map(int, input().split()))
disjoint = Disjoint(n)
for _ in range(m):
    a = list(input().split())
    if len(a) == 2:
        print(disjoint.get_min(int(a[1]) - 1), disjoint.get_max(int(a[1]) - 1), disjoint.get_ele(int(a[1]) - 1))
    else:
        disjoint.union(int(a[1]) - 1, int(a[2]) - 1)
