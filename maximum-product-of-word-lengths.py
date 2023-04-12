class Solution:
    def maxProduct(self, words: List[str]) -> int:
        for i, word in enumerate(words):
            bit_mask = 0
            for w in word:
                bit_mask |= (1 << (ord(w) - ord("a")))
            words[i] = [len(word), bit_mask]
        
        ans = 0
        for i, bit1 in words:
            for j, bit2 in words:
                if not (bit1 & bit2):
                    ans = max(ans, i * j)
        return ans