class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        start=1
        end=len(nums)-2
        ans=nums[0]+nums[-1]
        while start<end:
            if ans<nums[start]+nums[end]:
                ans=nums[start]+nums[end]
            start=start+1
            end=end-1
        return ans