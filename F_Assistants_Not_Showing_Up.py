n, m = list(map(int, input().split()))
pre = [0] * (n + 1)

for i in range(m):
    b, e = list(map(int, input().split()))
    pre[b] += 1
    pre[e + 1] -= 1

for i in range(1, n):
    pre[i] += pre[i - 1]

res = min(pre[:-1])

if res == 0:
    print("YES")
else:
    print("NO")