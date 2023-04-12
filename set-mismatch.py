class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        leng,result,tot=len(nums),[0,0],0
        num=[0]*leng
        for i in nums:
            if num[i-1]==1:
                result[0]=i
            num[i-1]+=1
            tot=tot+i
        total=leng*(leng+1)//2
        result[1]=result[0]+total-tot
        return result