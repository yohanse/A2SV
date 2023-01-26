n, m = list(map(int,input().split()))
res = []
for i in range(n):
    res.append(input().strip())
ans = ""
for i in range(n):
    for j in range(m):

        check = True

        for k in range(n):
            if k != i and res[i][j] == res[k][j]:
                check = False

        for k in range(m):
            if k != j and res[i][j] == res[i][k]:
                check = False
        if check:
            ans += res[i][j]
print(ans)