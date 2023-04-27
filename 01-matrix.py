class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        root, visite = [], set()
        for i in range(n):
            for j in range(m):
                if not mat[i][j]:
                    root.append((i, j))
                    visite.add((i, j))
        
        count = 0
        while root:
            temp = []
            for r, c in root:
                for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    x, y = r + dx, c + dy
                    if -1 < x < n and -1 < y < m and (x, y) not in visite:
                        temp.append((x, y))
                        visite.add((x, y))
                mat[r][c] = count
            count += 1
            root = temp
        return mat