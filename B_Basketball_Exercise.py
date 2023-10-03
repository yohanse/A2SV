n = int(input())

dp = [[0 for i in range(n + 1)] for j in range(2)]

for i in range(2):
    nums = list(map(int, input().split()))
    for j in range(n):
        dp[i][j + 1] = nums[j]

for i in range(2, n + 1):
    for j in range(2):
        dp[j][i] = max(max(dp[j][i - 2], dp[1 - j][i - 1]) + dp[j][i], dp[j][i - 1])
print(max(dp[0][-1], dp[1][-1]))

