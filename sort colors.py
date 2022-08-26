class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        number_zero=0
        number_one=0
        count=0
        for i in nums:
            if i==0:
                number_zero+=1
            elif i==1:
                number_one+=1
        for i in range(len(nums)):
            if count<number_zero:
                nums[i]=0
            elif count<number_one+number_zero:
                nums[i]=1
            else:
                nums[i]=2
            count=count+1