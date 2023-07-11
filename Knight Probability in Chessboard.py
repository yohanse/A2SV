class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = {}
        def rec(x, y, k):

            if not (-1 < x < n and -1 < y < n):
                return 0

            if k == 0:
                return 1
            
            if (x, y, k) in dp:
                return dp[(x, y, k)]
            
            dp[(x, y, k)] = 0
            for dx, dy in [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]:
                dp[(x, y, k)] += rec(x + dx, y + dy, k - 1)
            return dp[(x, y, k)]
            
        return rec(row, column, k) / 8 ** k

        