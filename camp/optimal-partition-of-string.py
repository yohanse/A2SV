class Solution:
    def partitionString(self, s: str) -> int:
        seen = group = 0
        for letter in s:
            shift = ord(letter) - ord("a")
            if (seen >> shift) & 1:
                seen = 0
                group += 1

            seen |= 1 << shift
        return group + 1 