class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        N = len(nums)
        index = {nums[i]:i for i in range(N)}
        for op1, op2 in operations:
            i = index.get(op1,0)
            nums[i] = op2
            index[op2] = i
        return nums