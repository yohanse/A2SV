class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        joo=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    count=count+1
            joo.append(count)
        return joo