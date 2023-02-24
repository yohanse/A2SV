class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        words, slow, res = set(), 0, 0
        for fast, letter in enumerate(s):
            while letter in words:
                words.remove(s[slow])
                slow += 1
            words.add(letter)
            res = max(res, fast - slow + 1)
        return res