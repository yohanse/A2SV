
import sys
n, d = list(map(int, input().split()))
nums = list(map(int, list(input())))


dp = [sys.maxsize] * n
dp[0] = 0
for i in range(1, n):
    if nums[i]:
        for j in range(max(0, i - d), i):
            if nums[j]:
                dp[i] = min(dp[i], dp[j] + 1)

if dp[-1] != sys.maxsize:
    print(dp[-1])
else:
    print(-1)