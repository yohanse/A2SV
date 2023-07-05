n, m = list(map(int, input().split()))
data = []
for i in range(n):
    a, b, c = list(map(int, input().split()))
    data.append((a - 1, b - 1, c))

data.sort()
ans = [[data[0][0], data[0][1], min(data[0][2], data[0][1] - data[0][0] + 1)]]

for start, end, interval in data[1:]:
    if start <= ans[-1][1]:
        ans[-1][1] = max(end, ans[-1][1])
        ans[-1][2] = min(min(interval, end - start + 1) + ans[-1][2], ans[-1][1] - ans[-1][0] + 1)
    else:
        ans.append([start, end, min(interval, end - start + 1)])

res = 0
for a, b, c in ans:
    res += c
res = m - res
print(res)
