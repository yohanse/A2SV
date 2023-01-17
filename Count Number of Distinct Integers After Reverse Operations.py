class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        num = set()
        for i in range(len(nums)):
            num.add(nums[i])
            num.add(int(str(nums[i])[::-1]))
        return len(num)