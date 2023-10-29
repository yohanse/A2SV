class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        left = [0 for i in range(n)]
        right = [0 for i in range(n)]

        for i in range(n):
            for j in range(n):
                left[i] = max(left[i], grid[i][j])
                right[j] = max(right[j], grid[i][j])
        ans = 0
        for i in range(n):
            for j in range(n):
                ans += min(left[i], right[j]) - grid[i][j]

        return ans 