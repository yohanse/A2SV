import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))
    grid = []
    for i in range(n):
        grid.append(list(map(int, input().split())))
    visite = set()
    final = 0
    for i in range(n):
        for j in range(m):
            if (i, j) not in visite and grid[i][j]:
                q = [(i, j)]
                visite.add((i, j))
                ans = 0
                while q:
                    r, c = q.pop()
                    ans += grid[r][c]
                    for dx, dy in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                        x, y = r + dx, c + dy
                        if -1 < x < n and -1 < y < m and (x, y) not in visite and grid[x][y] != 0:
                            visite.add((x, y))
                            q.append((x, y))
                final = max(final, ans)
    print(final)