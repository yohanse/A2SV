x = int(input())
tot = x
d = 2
res = [1, x]
ans = []
while d * d <= x:
    a = 1
    while x % d== 0:
        x //= d
        a *= d

    if a != 1:
        ans.append(a)
    d += 1
if x != 1:
    ans.append(x)

y = len(ans)



n = 2 ** y
for i in range(1, n):
    c = 0
    t = 1
    while i:
        if i & 1:
            t *= ans[c]
        i = i >> 1
        c += 1

    if max(res) > max(tot // t, t):
        res = [t, tot // t]
        
print(*res)
