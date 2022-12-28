class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        res = [[] for i in range(rows + cols - 1)]
        for r in range(rows):
            for c in range(cols):
                res[r + c].append(mat[r][c])
        res1 = []
        for i in range(rows + cols -1):
            if i%2 == 0:
                res[i].reverse()
            res1.extend(res[i])
        return res1