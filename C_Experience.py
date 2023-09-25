import sys
class Disjoint:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.score = [0 for _ in range(n)]
        
    def union(self, a, b):
        px, py = self.find(a), self.find(b)
        if px != py:
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1

            if self.rank[px] > self.rank[py]:
                self.parent[py] = px
                self.score[py] -= self.score[px]
            else:
                self.parent[px] = py
                self.score[px] -= self.score[py]

    def find(self, a):
        while a != self.parent[a]:
            a = self.parent[a]
        return a

    def getScore(self, a):
        ans = 0
        while a != self.parent[a]:
            ans += self.score[a]
            a = self.parent[a]
        return ans + self.score[a]
    
    def addScore(self, a, b):
        self.score[self.find(a)] += b


n, m = list(map(int, input().split()))
disjoint = Disjoint(n)
for _ in range(m):
    command = input().split()
    if command[0] == "add":
        disjoint.addScore(int(command[1]) - 1, int(command[2]))
    elif command[0] == "join":
        disjoint.union(int(command[1]) - 1, int(command[2]) - 1)
    else:
        print(disjoint.getScore(int(command[1]) - 1))
