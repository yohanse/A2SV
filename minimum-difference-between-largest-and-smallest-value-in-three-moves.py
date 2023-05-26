class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0
        nums.sort()
        r = len(nums) - 4
        l = 0
        ans = sys.maxsize
        for i in range(r, len(nums)):
            ans = min(nums[i] - nums[l], ans)
            l += 1
        return ans