class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        N, res = len(grid), 0
        for r in range(N):
            for c in range(N):
                for k in range(N):
                    if grid[r][k] != grid[k][c]:
                        break
                else:
                    res += 1
        return res