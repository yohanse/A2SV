class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])

        direction = {
            1:[[0, -1, 4], [0, -1, 6], [0, -1, 1], [0, 1, 3], [0, 1, 5], [0, 1, 1]], 
            2:[[1, 0, 5], [1, 0, 2], [1, 0, 6], [-1, 0, 3], [-1, 0, 4], [-1, 0, 2]], 
            3:[[0, -1, 4], [0, -1, 6], [0, -1, 1], [1, 0, 5], [1, 0, 6], [1, 0, 2]], 
            4:[[1, 0, 5], [1, 0, 6], [1, 0, 2], [0, 1, 3], [0, 1, 5], [0, 1, 1]], 
            5:[[-1, 0, 3], [-1, 0, 4], [-1, 0, 2], [0, -1, 4], [0, -1, 6], [0, -1, 1]],
            6:[[-1, 0, 3], [-1, 0, 4], [-1, 0, 2], [0, 1, 3], [0, 1, 5], [0, 1, 1]]
            }

        q = deque([(0, 0)])
        visite = set([(0, 0)])
        while q:
            r, c = q.popleft()
            if r == n - 1 and c == m - 1:
                return True
            for dx, dy, typ in direction[grid[r][c]]:
                x, y = r + dx, c + dy

                if -1 < x < n and -1 < y < m and (x, y) not in visite and typ == grid[x][y]:
                    visite.add((x, y))
                    q.append((x, y))
        return False