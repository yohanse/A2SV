class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans=''
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        def compare(a,b):
            if a+b>b+a:
                return -1
            else:
                return 1
        nums=sorted(nums,key=cmp_to_key(compare))
        for i in nums:
            ans=ans+str(i)
        return str(int(ans))