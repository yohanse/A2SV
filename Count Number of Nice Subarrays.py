class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd=[-1]
        for i,num in enumerate(nums):
            if num%2!=0:
                odd.append(i)
        odd.append(len(nums))
        ans=0
        count=1
        while count<len(odd)-1:
            if count>=k:
                ans=ans+((odd[count+1]-odd[count])*(odd[count-k+1]-odd[count-k]))
            count=count+1
        return ans