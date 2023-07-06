class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = []
        for i in range(query_row + 1):
            dp.append([0 for i in range(i + 1)])
        dp[0][0] = poured

        for i in range(query_row):
            for j in range(i + 1):
                dp[i + 1][j] += max(0, (dp[i][j] - 1) / 2)
                dp[i + 1][j + 1] += max(0, (dp[i][j] - 1) / 2)

        return min(1, dp[query_row][query_glass])
