class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        maxx = 0
        for diff in range(-501, 501):
            dp = {}
            for x in nums:
                dp[x] = dp.get(x - diff, 0) + 1
                maxx = max(dp[x], maxx)
        return maxx