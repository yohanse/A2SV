class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans,tot,l=0,0,0
        for r,num in enumerate(nums):
            tot+=num
            while num*(r-l+1)>tot+k:
                tot-=nums[l]
                l+=1
            ans=max(ans,r-l+1)
        return ans