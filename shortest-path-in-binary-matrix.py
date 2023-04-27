class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        direction = [[1, 0], [0, 1], [1, 1], [-1, 0], [0, -1], [-1, -1], [1, -1], [-1, 1]]
        if grid[-1][-1] or grid[0][0]:
            return -1

        q = deque([(0, 0, 1)])
        grid[0][0] = 1

        while q:
            r, c, cou = q.popleft()
            if r == n - 1 == c:
                return cou

            for dx, dy in direction:
                x, y = r + dx, c + dy
                if -1 < x < n and -1 < y < n and grid[x][y] == 0:
                    grid[x][y] = 1
                    q.append((x, y, cou + 1))
        return -1