class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans,slow,fast=0,0,0
        length=len(nums)
        while fast<length:
            if nums[fast]==0:
                if k>0:
                    k=k-1
                else:
                    while nums[slow]!=0:
                        slow=slow+1
                    slow=slow+1
            ans=max(1+fast-slow,ans)
            fast=fast+1
        return ans