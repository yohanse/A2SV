class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        N = len(piles) // 3
        tot = 0
        for i in range(N, 3*N, 2):
            tot += piles[i]
        return tot