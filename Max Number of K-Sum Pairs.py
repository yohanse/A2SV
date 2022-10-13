class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        end=len(nums)-1
        start=0
        count=0
        while start<end:
            if nums[start]+nums[end]==k:
                count=count+1
                end=end-1
                start=start+1
            elif nums[start]+nums[end]>k:
                end=end-1
            else:
                start=start+1
        return count