class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n, m = len(maze), len(maze[0])

        q = deque([(entrance[0], entrance[1], 0)])
        while q:
            r, c, count = q.popleft()
            if r == 0 or c == 0 or r == n - 1 or c == m -1:
                if entrance[0] != r or entrance[1] != c:
                    return count
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                x, y = r + dx, c + dy
                if -1 < x < n and -1 < y < m and maze[x][y] == ".":
                    maze[x][y] = "+"
                    q.append((x, y, count + 1))
        return -1