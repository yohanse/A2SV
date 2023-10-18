class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        ans = 0
        for i in range(n):
            if word[i] in "aeiou":
                ans += ((i + 1) * (n - i))
        return ans