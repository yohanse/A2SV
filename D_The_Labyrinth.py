import sys

input = sys.stdin.readline

class Disjoint:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
            self.rank[px] += 1
        else:
            self.parent[px] = py
            self.rank[py] += 1
        
    
    def find(self, x):
        y = x
        while x != self.parent[x]:
            x = self.parent[x]

        while y != self.parent[y]:
            y = self.parent[y]
            self.parent[y] = x

        return x

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)


n, m = list(map(int, input().split()))
graph = [[0 for i in range(m)] for j in range(n)]
ans = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    x = input()
    for j in range(m):
        graph[i][j] = x[j]


disjoint = Disjoint(n * m)
for i in range(n):
    for j in range(m):
        if graph[i][j] == '.':
            for dx, dy in  [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                x, y = i + dx, j + dy
                if -1 < x < n and -1 < y < m and graph[x][y] == '.' :
                    disjoint.union(x * m + y, i * m + j)



visite1 = set()
for i in range(n):
    for j in range(m):
        if graph[i][j] == '.' and (i, j) not in visite1:
            s = [(i, j)]
            visite = set([(i, j)])
            while s:
                r, c = s.pop()
                for dx, dy in  [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    x, y = r + dx, c + dy
                    if -1 < x < n and -1 < y < m and graph[x][y] == '.' and (x, y) not in visite:
                        s.append((x, y))
                        visite.add((x, y))
                visite1.add((r, c))

            for k, l in visite:
                ans[k][l] = len(visite)


result = [['.' for i in range(m)] for j in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == '*':
            result[i][j] = 0
            visite = set()
            for dx, dy in  [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                x, y = i + dx, j + dy
                if -1 < x < n and -1 < y < m and graph[x][y] == '.':
                    visite.add(disjoint.find(x * m + y))
            for z in visite:
                result[i][j] += ans[z // m][z % m]
            result[i][j] += 1
            result[i][j] %= 10
for i in result:
    print(*i, sep = '')


