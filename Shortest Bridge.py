class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q1, q = deque(), deque()
        direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        def give():
            for i in range(n):
                for j in range(n):
                    if grid[i][j]:
                        q1.append((i, j))
                        grid[i][j] = "x"
                        return
        give()     
        while q1:
            r, c = q1.popleft()
            q.append((r, c, 0))
            for dx, dy in direction:
                x, y = r + dx, c + dy
                if -1 < x < n and -1 < y < n and grid[x][y] == 1:
                    grid[x][y] = "x"
                    q1.append((x, y))
            
        while q:
            r, c, count = q.popleft()

            for dx, dy in direction:
                x, y = r + dx, c + dy
                if -1 < x < n and -1 < y < n and grid[x][y] != "x":

                    if grid[x][y] == 1:
                        return count

                    grid[x][y] = "x"
                    q.append((x, y, count + 1))