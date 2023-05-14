class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        q = [(matrix[0][0], 0, 0)]
        visite = set([(0, 0)])
        for i in range(k - 1):
            value, r, c = heappop(q)
            if r + 1 < len(matrix) and (r + 1, c) not in visite:
                heappush(q, (matrix[r + 1][c], r + 1, c))
                visite.add((r + 1, c))
            if c + 1 < len(matrix) and (r, c + 1) not in visite:
                heappush(q, (matrix[r][c + 1], r, c + 1))
                visite.add((r, c + 1))
        return heappop(q)[0]