class Solution:
    def is_possible(self, cells, row, col, final):
        matrix = matrix = [[1 for i in range(col)] for j in range(row)]
        stack = []
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for i in range(final):
            matrix[cells[i][0] - 1][cells[i][1] - 1] = 0

        for i in range(col):
            if matrix[0][i]:
                matrix[0][i] = 0
                stack.append((0, i))
                
        while stack:
            r, c = stack.pop()
            if r == row - 1:
                return True
            for dx, dy in direction:
                x, y = r + dx, c + dy
                if -1 < x < row and -1 < y < col and matrix[x][y]:
                    matrix[x][y] = 0
                    stack.append((x, y))
        return False

        
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        l, r = 0, row * col - 1

        while l < r:
            mid = (l + r) // 2
            if self.is_possible(cells, row, col, mid + 1):
                l = mid + 1
            else:
                r = mid
        return r