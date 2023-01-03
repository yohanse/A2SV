class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [0]*N
        for i in range(N):
            res[i] = nums[nums[i]]
        return res 