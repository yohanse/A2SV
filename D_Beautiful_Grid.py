t = int(input())
for r in range(t):

    n = int(input())
    res = []
    for c in range(n):
        m = input()
        res.append(m)
    op1 = 0
    for i in range(n):
        for j in range(n):
            table = [res[i][j], res[j][n-i-1], res[n-i-1][n-j-1], res[n-j-1][i]]
            c, c1= 0, 0
            for p in table:
                if p == "1":
                    c += 1
                else:
                    c1 += 1
            op1 += min(c, c1)
    print(op1//4)
    