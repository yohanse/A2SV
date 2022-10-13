class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        ans=0
        count=1
        for i in range(len(piles)//3):
            ans=ans+piles[count]
            count=count+2
        return ans