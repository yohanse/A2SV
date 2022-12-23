class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        N=len(nums)
        res=0
        for i in range(2,N):
            if nums[i-2]+nums[i-1]>nums[i] and nums[i]+nums[i-1]>nums[i-2] and nums[i-2]+nums[i]>nums[i-1]:
                res=max(res,nums[i-1]+nums[i]+nums[i-2])
        return res