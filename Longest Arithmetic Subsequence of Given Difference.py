class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        for val in arr:
            dp[val] = dp.get(val - difference, 0) + 1
        return max(dp.values())
        