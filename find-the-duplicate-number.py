class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i + 1:
                index = nums[i] - 1
                nums[index], nums[i] = nums[i], nums[index]
                if nums[index] == nums[i]:
                    return nums[index]