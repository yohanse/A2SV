n, m  = list(map(int, input().split()))

grid = []
for i in range(n):
    grid.append(list(input()))

horizontal, verteical = [[] for i in range(n)], [[] for i in range(m)]
count = 0
for r in range(n):
    for c in range(m):
        if grid[r][c] == "*":
            count += 1
for r in range(n):
    for c in range(m):
        if grid[r][c] == "*":
            i, j = r, c
            