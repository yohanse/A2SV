class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        N = len(nums)
        def rec(i, tot):
            if i == N:
                return tot == target

            if (i, tot) in dp:
                return dp[(i, tot)]
                
            dp[(i, tot)] = rec(i + 1, tot + nums[i]) + rec(i + 1, tot - nums[i])
            return dp[(i, tot)]

        return rec(0, 0)