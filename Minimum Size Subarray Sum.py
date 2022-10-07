class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=0
        slow=0
        tot=0
        first=True
        for i,value in enumerate(nums):
            tot=tot+value
            while tot>=target:
                if first:
                    ans=i-slow+1
                ans=min(ans,i-slow+1)
                tot=tot-nums[slow]
                slow=slow+1
                first=False
        return ans