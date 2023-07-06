class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [[1, 1] for i in range(N)]
        for i in range(N):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i][0] = max(dp[j][1] + 1, dp[i][0])
                elif nums[j] > nums[i]:
                    dp[i][1] = max(dp[j][0] + 1, dp[i][1])
        ans = 1
        for a, b in dp:
            ans = max(ans, a, b)
        return ans