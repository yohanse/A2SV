class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def palindrome(l, r):
            if r <= l:
                return 1 if l == r else 0

            if s[l] == s[r]:
                return palindrome(l + 1, r - 1) + 2

            return max(palindrome(l + 1, r), palindrome(l, r - 1))

        return palindrome(0, len(s) - 1)