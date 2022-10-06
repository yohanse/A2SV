class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        pass_zero=False
        slow=0
        leng=len(nums)
        stack=[]
        ans=0
        for i in range(leng):
            if nums[i]==0:
                stack.append(i)
                if pass_zero==True:
                    slow=stack[0]
                    slow=slow+1
                    stack=stack[1:]
                    
                else:
                    pass_zero=True
            ans=max(ans,i-slow)
        return ans