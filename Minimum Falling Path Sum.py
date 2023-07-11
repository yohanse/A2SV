class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for r in range(1,n):
            for c in range(n):
                if c-1 > -1 and c+1 < n:
                    matrix[r][c] += min(matrix[r-1][c], matrix[r-1][c+1], matrix[r-1][c-1])
                elif c-1 > -1:
                    matrix[r][c] += min(matrix[r-1][c], matrix[r-1][c-1])
                else:
                    matrix[r][c] += min(matrix[r-1][c], matrix[r-1][c+1])

        res = sys.maxsize
        for i in range(n):
            res = min(res, matrix[-1][i])
        return res