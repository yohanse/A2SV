class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        joo=[]
        count=0
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        for i in nums:
            if i==target:
                joo.append(count)
            count=count+1
        return joo