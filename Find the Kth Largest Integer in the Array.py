class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        for i,value in enumerate(nums):
            nums[i]=int(value)
        nums.sort()
        leng=len(nums)
        return str(nums[leng-k])