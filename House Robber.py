class Solution:
    def rob(self, nums: List[int]) -> int:
        N=len(nums)
        dp={}
        def dynamic(n):
            if n>=N:
                return 0
            elif n in dp:
                return dp[n]
            dp[n]=max(dynamic(n+2)+nums[n],dynamic(n+3)+nums[n])
            return dp[n]
        return max(dynamic(0),dynamic(1))