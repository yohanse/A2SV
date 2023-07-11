class Solution:
    def numTrees(self, n: int) -> int:
        dp ={1: 1}
        def rec(l, r):
            check = r - l + 1
            if check in dp:
                return dp[check]

            num = 0
            for i in range(l, r + 1):
                left = rec(l, i - 1)
                right = rec(i + 1, r)
                num += left * right
            
            if num == 0:
                dp[check] = 1
                return 1
            dp[check] = num
            return num
        return rec(1, n)