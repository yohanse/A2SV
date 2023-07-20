class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums.sort()
        target.sort()
        N = len(nums)
        odd_nums, even_nums = [], []
        odd_target, even_target = [], []
        for i in range(N):
            if target[i] % 2:
                odd_target.append(target[i])
            else:
                even_target.append(target[i])

            if nums[i] % 2:
                odd_nums.append(nums[i])
            else:
                even_nums.append(nums[i])

        

        res = 0

        for i in range(len(odd_nums)):
            res += abs(odd_nums[i] - odd_target[i]) // 2

        for i in range(len(even_target)):
            res += abs(even_target[i] - even_nums[i]) // 2

        return res // 2
