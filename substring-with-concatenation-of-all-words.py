class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res, word_length, s_length, each_length = [], len(words), len(s), len(words[0])
        total, window = Counter(words), Counter(words)
        need, have = len(total), 0
        for i in range(0,s_length):
            word, temp = s[i:i+each_length], i
            while word in window and window[word] > 0:
                window[word] -= 1
                have += 1 if window[word]==0 else 0 
                temp += each_length
                word = s[temp:temp+each_length]
            if have == need:
                res.append(i)
            window = total.copy()
            have = 0
            if temp == s_length:
                break
        return res