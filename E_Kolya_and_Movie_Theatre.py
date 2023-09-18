t = int(input())
for _ in range(t):
    n, m, d = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    dp = [[0, 0, 0] for i in range(n + 1)]

    for i in range(n):
        dp[i + 1][0] = max(dp[i - 1])