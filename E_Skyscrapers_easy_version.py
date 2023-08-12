n = int(input())
m = list(map(int, input().split()))

decreasing = [0 for i in range(n)]
increasing = [0 for i in range(n)]


decreasing[0] = m[0]
for i in range(1, n):
    decreasing[i] = min(decreasing[i - 1], m[i])


increasing[-1] = m[-1]
for i in range(n - 2, -1, -1):
    increasing[i] = min(increasing[i + 1], m[i])

ans = [0, 0]
for i in range(1, n - 1):
    if increasing[i + 1] < m[i] sum(decreasing[:i]) + sum(increasing[i:]) > ans[1]:
        ans = [i, sum(decreasing[:i]) + sum(increasing[i:])]

for i in range(n):
    if i < ans[0]:
        print(decreasing[i], end = " ")
    else:
        print(increasing[i], end = " ")
