class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        leng=len(nums)+1
        num=[0]*(leng)
        tot=0
        for start,end in requests:
            num[start]+=1
            num[end+1]-=1
        for i in range(leng):
            tot=tot+num[i]
            num[i]=tot
        tot=0
        num.sort(reverse=True)
        nums.sort(reverse=True)
        for i in range(len(nums)):
            tot+=(nums[i]*num[i])
        module=1000000007
        return tot%module
            