class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        tot = sum(grid[0]) + sum(grid[1])
        
        N = len(grid[1])
        for i in range(N - 2, -1, -1):
            grid[1][i] += grid[1][i + 1]

        for i in range(1, N):
            grid[0][i] += grid[0][i - 1]

        answer = sys.maxsize
        for i in range(N):
            answer = min(answer, max(grid[0][-1] - grid[0][i], grid[1][0] - grid[1][i]))

        return answer