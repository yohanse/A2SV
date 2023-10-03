import sys


n = int(input())


color = list(map(int, input().split()))
color.append(-1)
connected = []
l = 0
for r in range(n + 1):
    if color[l] != color[r]:
        connected.append(color[l])
        l = r

n = len(connected)
maxiConnected = [[1 for i in range(n)] for j in range(n)]
for i in range(n):
    dic = {}
    dic[connected[i]] = dic.get(connected[i], 0) + 1
    for j in range(i + 1, n):
        dic[connected[j]] = dic.get(connected[j], 0) + 1
        maxiConnected[j][i] = max(maxiConnected[j - 1][i], dic[connected[j]])

dp = [sys.maxsize for i in range(n + 1)]
dp[0] = 0
for i in range(1, n + 1):
    for j in range(i):
        dp[i] = min(dp[i], dp[j] + i - j - maxiConnected[i - 1][j] + 1)
print(dp[-1] - 1)