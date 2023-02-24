class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tot=sum(nums[:k])
        ans=tot
        for i in range(len(nums)-k):
            tot=tot-nums[i]+nums[i+k]
            ans=max(ans,tot)
        return ans/k