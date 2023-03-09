
import sys


t = int(input())
for i in range(t):
    n = int(input())
    weight = list(map(int, input().split()))
    for i in range(1, n):
        weight[i] += weight[i - 1]
    dp = [False] *(n + 1)
    dp[0] = True
    weight = [0] + weight

    num = sys.maxsize
    for i in range(n + 1):
        if i - 12 > -1 and dp[i - 12]:
            num = min(weight[i] - weight[i - 12], num)
            dp[i] = True

        if i - 18 > -1 and dp[i - 18]:
            num = min(weight[i] - weight[i - 18], num)
            dp[i] = True

    for i in range(n):
        if dp[i]:
            num = min(num, weight[-1] - weight[i])

    print(num)  