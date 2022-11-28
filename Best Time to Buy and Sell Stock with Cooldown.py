class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N,dpl=len(prices),{}
        def dp(pos,buy,last):
            if pos>=N:
                if buy:return prices[last]
                return 0
            elif (pos,buy) in dpl:
                return dpl[(pos,buy)]
            elif not buy:
                dpl[(pos,False)]=max(dp(pos+1,False,last),dp(pos+1,True,pos)-prices[pos])
                return dpl[(pos,False)]
            dpl[(pos,True)]=max(dp(pos+1,True,last),dp(pos+2,False,last)+prices[pos])
            return dpl[(pos,True)]
        return dp(0,False,0)
        