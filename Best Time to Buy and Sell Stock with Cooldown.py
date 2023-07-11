class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = [0 for i in range(N + 2)]

        for i in range(1, N):
            dp[i + 2] = dp[i + 1]
            for j in range(i):
                dp[i + 2] = max(dp[i + 2], max(0, prices[i] - prices[j]) + dp[j])
        return max(dp)
        