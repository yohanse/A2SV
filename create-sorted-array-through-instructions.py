class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums, cost = [], 0
        for num in instructions:
            cost += min(len(nums) - bisect_right(nums, num), bisect_right(nums, num - 1))
            cost %= 10**9 + 7
            insort(nums, num)
        return cost