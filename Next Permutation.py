class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        leng=len(nums)
        count=0
        for i in range(leng-1,0,-1):
            if nums[i-1]<nums[i]:
                count=i
                break
        if count==0:
            nums.sort()
            return
        j=leng-1
        while nums[count-1]>=nums[j]:
            j=j-1
        nums[j],nums[count-1]=nums[count-1],nums[j]
        end=leng-1
        start=count
        while start<end:
            nums[end],nums[start]=nums[start],nums[end]
            start=start+1
            end=end-1