t = int(input())
for i in range(t):
    n, m = list(map(int, input().split()))
    res = [[0 for i in range(m)] for j in range(n)]
    test = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if (i + j) % 2:
                res[i][j] = 1

    for i in range(2, n, 4):
        res[i], res[i + 1] = res[i + 1], res[i]
    
    for i in range(n):
        for j in range(2, m, 4):
            res[i][j], res[i][j + 1] = res[i][j + 1], res[i][j]

    for i in range(n):
        print(*res[i])