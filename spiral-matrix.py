class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        count = 0
        res = []
        dx, dy = 0, 1
        r, c = 0, 0
        while count < m * n:
            if -1 < r < n and -1 < c < m and matrix[r][c] != "#":
                res.append(matrix[r][c])
                matrix[r][c] = "#"
                r, c = r + dx, c + dy
                count += 1

            else:
                r, c = r - dx, c - dy
                dx, dy = dy, -dx
                r, c = r + dx, c + dy
        return res