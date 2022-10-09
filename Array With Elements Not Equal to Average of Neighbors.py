class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        resul=[]
        start,end=0,len(nums)-1
        while start<end:
            resul.append(nums[start])
            resul.append(nums[end])
            start=start+1
            end=end-1
        if start==end:
            resul.append(nums[start])
        return resul