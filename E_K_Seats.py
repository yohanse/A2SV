n, m, k = list(map(int, input().split()))
res = []
for i in range(n):
    res.append(input())
def f(s, k):
    p = len(s)
    c = 0
    ans = 0
    for i in range(p):
        if s[i] == '.':
            c += 1
        else:
            c = 0
        if c >= k:
            ans += 1
    return ans
ans = 0
for i in range(n):
    ans += f(res[i], k)

for j in range(m):
    o = ""
    for i in range(n):
        o += res[i][j]
    ans += f(o, k)
    
print(ans)
