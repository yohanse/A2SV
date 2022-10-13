class Solution:
    def check(self,num):
        num.sort()
        k=num[1]-num[0]
        for i in range(1,len(num)):
            if num[i]-num[i-1]!=k:
                return False
        return True
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans1=[]
        for i,j in zip(l,r):
            ans=self.check(nums[i:j+1])
            ans1.append(ans)
        return ans1