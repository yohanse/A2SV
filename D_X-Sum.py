t = int(input())
for i in range(t):
    negative = {}
    positive = {}
    res = []
    n, m = list(map(int,input().split()))
    for r in range(n):
        num = list(map(int,input().split()))
        res.append(num)
        for c in range(m):
            positive[r + c] = num[c] + positive.get(r+c, 0)
            negative[r - c] = num[c] + negative.get(r-c, 0)
    
    res1 = 0
    for i in range(n):
        for j in range(m):
            res1 = max(res1, negative[i - j] + positive[i + j] - res[i][j])
    print(res1)
        

