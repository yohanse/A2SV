class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length=len(nums)
        while k>length:
            k=k-length
        nums.extend(nums[:length-k])
        for i in range(length-k):
            nums.pop(0)