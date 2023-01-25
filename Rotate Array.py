class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        temp = nums.copy()
        for i in range(N):
            nums[(i + k)%N] = temp[i]