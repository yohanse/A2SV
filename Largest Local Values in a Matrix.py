class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        def maximum(r,c):
            res = 0
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    res = max(res,grid[i][j])
            return res

        res = [[0 for _ in range(n - 2)] for _ in range(n - 2)]
        for r in range(n - 2):
            for c in range(n -2):
                res[r][c] = maximum(r,c)

        return res 