class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tot=1
        leng=len(nums)
        ans=[None]*leng
        for i,value in enumerate(nums):
            ans[i]=tot
            tot=tot*value
        tot=1
        for i in range(leng-1,-1,-1):
            ans[i]=ans[i]*tot
            tot=tot*nums[i]
        return ans