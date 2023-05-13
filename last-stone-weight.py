class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while stones and len(stones) != 1:
            x, y = -heapq.heappop(stones), -heapq.heappop(stones)
            if x != y:
                x -= y
                heapq.heappush(stones, -x)
        if stones:
            return -stones[-1]
        return 0