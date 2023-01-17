n, m = list(map(int,input().split()))
res = []
for i in range(n):
    num = input()
    num = list(num)
    res.append(num)

for i in range(n):
    for j in range(m):
        if res[i][j] == 'S':
            ini, fin = i , j
            break

direction = [[0,1], [1,0], [-1,0],[0,-1]]
q = [[ini, fin, 0, 0, 0]]
op = 'NO'
r = 0
while q:
    r, c, p1, p2, ans = q.pop(0)
    
    if res[r][c] == 'T':
        if ans <= 2:
            op = 'YES'
        continue
            
    if res[r][c] != 'T':
            res[r][c] = '*'
        
    for i, j in direction:
        n_r, n_c = i + r, j + c
        if -1<n_r<n and -1<n_c<n and res[n_r][n_c]!='*':
            if p1 == 0 and p2 == 0:
                q.append([n_r, n_c, i, j, ans])
            else:
                if p1 != i or p2 != j:
                    q.append([n_r, n_c, i, j, ans + 1])
                else:
                    q.append([n_r, n_c, i, j, ans])
            
print(op)

