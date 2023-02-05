t = int(input())
for i in range(t):
    n, m = list(map(int,input().split()))
    res= []
    for j in range(n):
        res.append(list(input()))
    final = [['.' for j in range(m)] for i in range(n)]
    for i in range(m):
        p = n - 1
        for j in range(n - 1, -1, -1):
            if res[j][i] == '*':
                final[p][i] = '*'
                p -= 1
            elif res[j][i] == 'o':
                final[j][i] = 'o'
                p = j - 1
    for i in range(n):
        print(''.join(final[i]))
    

