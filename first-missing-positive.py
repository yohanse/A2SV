class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(len(nums)):
            while 0 < nums[i] < N and nums[i] != i + 1:
                index = nums[i] - 1
                nums[i], nums[index] = nums[index], nums[i]
                if nums[i] == nums[index]:
                    break

        for i in range(N):
            if i + 1 != nums[i]:
                return i + 1
        return N + 1