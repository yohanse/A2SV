class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        leng=len(cost)
        dp={}
        def rec(n):
            if n<2:
                return 0
            if n in dp:return dp[n]
            dp[n]=min(rec(n-2)+cost[n-2],rec(n-1)+cost[n-1])
            return dp[n]
        return rec(leng)