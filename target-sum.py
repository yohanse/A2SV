class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        leng=len(nums)
        table={}
        def back(target,num,leng,i=0,tot=0):
            if i==leng:
                if target!=tot:
                    return 0
                return 1
            if (i,tot) in table:
                return table[(i,tot)]
            table[(i,tot)]=back(target,num,leng,i+1,tot+num[i])+back(target,num,leng,i+1,tot-num[i])
            return table[(i,tot)]
        return back(target,nums,leng)