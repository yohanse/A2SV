class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        def dp(rating):
            ans = 0
            dp = [0 for i in range(n)]

            for i in range(n):
                for j in range(i):
                    if rating[i] > rating[j]:
                        ans += dp[j]
                        dp[i] += 1
            return ans
        return dp(rating) + dp(rating[::-1])