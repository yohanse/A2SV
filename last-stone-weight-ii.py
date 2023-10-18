class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        visited = set([0])

        for i in range(len(stones)):
            copyVisited = set()

            for value in visited:
                copyVisited.add(value - stones[i])
                copyVisited.add(value + stones[i])
            visited = copyVisited
        ans = float("inf")

        for val in visited:
            if val >= 0:
                ans = min(ans, val)
        return ans