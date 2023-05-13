class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        total = sum(piles)
        piles = [-i for i in piles]
        heapq.heapify(piles)
        for i in range(k):
            num = heapq.heappop(piles)
            total -= -num//2
            num += -num//2
            heapq.heappush(piles,num)
        return total