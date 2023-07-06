class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        nums.sort()

        for t in range(1, target+1):
            for num in nums:
                if t >= num:
                    dp[t] += dp[t - num]
                else:
                    break

        return dp[target]