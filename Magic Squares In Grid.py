class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def valid(r,c):
            visite = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
            for i in range(r,r+3):
                for j in range(c,c+3):
                    if grid[i][j] not in visite:
                        return False
                    visite.remove(grid[i][j])

            res = []
            for i in range(r,r+3):
                res.append(grid[i][c] + grid[i][c+1] + grid[i][c+2])

            for i in range(c,c+3):
                res.append(grid[r][i] + grid[r+1][i] + grid[r+2][i])

            res.append(grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2])
            res.append(grid[r][c + 2] + grid[r+1][c+1] + grid[r+2][c])
            
            for i in range(1,8):
                if res[i-1] != res[i]:
                    return False
            return True
        
        res = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                if valid(i,j):
                    print(i,j)
                    res += 1
        return res          