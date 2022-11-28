class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        num1=num2=prices[0]
        ans=0
        for i in prices:
            if i<num1:
                num1=num2=i
            num2=max(num2,i)
            ans=max(ans,num2-num1)
        return ans
    