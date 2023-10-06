class Solution:
    def knightDialer(self, n: int) -> int:
        modulo = 10 ** 9 + 7
        @cache
        def dfs(i, r, c):
            
            if r > 3 or r < 0 or c > 2 or c < 0 or (r == 3 and c != 1):
                return 0

            if i == n:
                return 1

            ans = 0
            for dx, dy in [[1, 2], [2, 1], [-1, 2], [2, -1], [-2, 1], [1, -2], [-1, -2], [-2, -1]]:
                ans += dfs(i + 1, r + dx, c + dy)
            return ans % modulo
        ans = 0
        for i in range(4):
            for j in range(3):
                ans += dfs(1, i, j)
        return ans % modulo