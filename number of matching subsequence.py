class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        N = len(s)
        dp = [[sys.maxsize for i in range(26)] for j in range(N + 1)]

        for i in range(N - 1, -1, -1):
            for j in range(26):
                dp[i][j] = dp[i + 1][j]
            dp[i][ord(s[i]) - ord('a')] = i
        
        def checker(string):
            k = j = 0
            while j < len(string) and dp[k][ord(string[j]) - ord('a')] != sys.maxsize:
                k = dp[k][ord(string[j]) - ord('a')] + 1
                j += 1
            return j == len(string)
        
        ans = 0
        for w in words:
            ans += checker(w)
        return ans              