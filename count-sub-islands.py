class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        row,col=len(grid1),len(grid1[0])
        def bfs(r,c):
            queue = deque([(r,c)])
            check = 1
            while queue:
                r, c = queue.popleft()
                if grid1[r][c] == 0:
                    check=0

                for i, j in [[0,1], [0,-1], [1,0], [-1,0]]:
                    nr, nc = r + i, c + j
                    if -1 < nr < row and -1 < nc < col and grid2[nr][nc] == 1:
                        grid2[nr][nc] = 0
                        queue.append((nr,nc))

            return check

        res=0
        for r in range(row):
            for c in range(col):
                if grid2[r][c] == 1:
                    res += bfs(r,c)
        return res