n, m = list(map(int, input().split()))

final = 10 ** 2 + 2
grid = [[0 for i in range(10 ** 2 + 2)]for j in range(10 ** 2 + 2)]

for _ in range(n):
    x, y = list(map(int, input().split()))
    grid[x + 1][y + 1] += 1

for i in range(1, final):
    for j in range(1, final):
        grid[i][j] += grid[i - 1][j] + grid[i][j - 1] - grid[i - 1][j - 1]


for j in range(m):
    x0, y0, x1, y1 = list(map(int, input().split()))
    print(grid[x1 + 1][y1 + 1] + grid[x0][y0] - grid[x1 + 1][y0] - grid[x0][y1 + 1])