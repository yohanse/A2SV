class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(ages)
        index = [[ages[i], scores[i]] for i in range(n)]
        index.sort()

        dp = [0 for i in range(n)]
        
        for i in range(n):
            for j in range(i):
                if index[i][1] >= index[j][1] or index[i][0] == index[j][0]:
                    dp[i] = max(dp[i], dp[j] + index[i][1])
            dp[i] = max(dp[i], index[i][1])
        return max(dp)
        