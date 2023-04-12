class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:

                index = nums[i] - 1
                nums[i], nums[index] = nums[index], nums[i]
        
        res = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(i + 1)

        return res