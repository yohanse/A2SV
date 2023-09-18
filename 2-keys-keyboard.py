class Solution:
    def minSteps(self, n: int) -> int:
        dp = [inf for i in range(n)]
        dp[0] = 0

        for i in range(2, n + 1):
            for j in range(1, i):
                if i % j == 0:
                    dp[i - 1] = min(dp[i - 1], dp[j - 1] + (i // j))
        return dp[-1]