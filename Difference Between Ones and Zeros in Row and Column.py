class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        res = [[-rows-cols for c in range(cols)] for r in range(rows)]
        for c in range(1,cols):
            grid[0][c] += grid[0][c-1]
        for r in range(1,rows):                             # to know prefix sum
            grid[r][0] += grid[r-1][0]
        for r in range(1,rows):
            for c in range(1,cols):
                grid[r][c] += grid[r-1][c] + grid[r][c-1] - grid[r-1][c-1]


        for r in range(rows):
            for c in range(cols):
                if r > 0 and c > 0:
                    res[r][c] += 2*((grid[r][-1] - grid[r-1][-1]) + (grid[-1][c] - grid[-1][c-1] ))
                elif r > 0:
                    res[r][c] += 2*((grid[r][-1] - grid[r-1][-1]) + grid[-1][c])   # compute result
                elif c > 0:
                    res[r][c] += 2*(grid[r][-1]  + (grid[-1][c] - grid[-1][c-1] ))
                else:
                    res[r][c] += 2*(grid[r][-1] + grid[-1][c] )
        return res