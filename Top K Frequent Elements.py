class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        length=len(nums)
        count=0
        candidate=nums[0]
        ans=[]
        ret=[]
        for i in range(length):
            if nums[i]==candidate:
                count=count+1
            else:
                ans.append([count,candidate])
                count=1
                candidate=nums[i]
        ans.append([count,candidate])
        ans.sort(reverse=True)
        for i in range(k):
            ret.append(ans[i][1])
        return ret