class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length=len(nums)
        total=0
        for i in range(length):
            total=total+nums[i]
            nums[i]=total
        for i in range(length):
            rightsum=total-nums[i]
            if i<=0:
                leftsum=0
            else:
                leftsum=nums[i-1]
            if rightsum==leftsum:
                return i
        return -1