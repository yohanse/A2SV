class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        count = 0
        currAND = 2 ** 32 - 1
        for num in nums:
            currAND &= num
            if currAND == 0:
                count += 1
                currAND = 2 ** 32 - 1
        return max(1, count)