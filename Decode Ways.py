class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        N = len(s)
        dp = [0 for i in range(N)]
        dp[0] = 1

        for i in range(1, N):
            if s[i] == s[i - 1] == "0":
                return 0
            
            if s[i] != "0":
                dp[i] += dp[i - 1]

            if s[i - 1] != "0" and int(s[i - 1] + s[i]) < 27:
                if i < 2:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - 2]

    
        return dp[-1]

