class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor, N = 0, len(nums)
        for i in range(len(nums)):
            xor ^= (i + 1) ^ nums[i]
        return xor