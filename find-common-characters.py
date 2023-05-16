class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        def count(word):
            res = [0]*26
            for i in range(len(word)):
                res[ord(word[i]) - 97] += 1
            return res
        for i in range(len(words)):
            words[i] = count(words[i])
        res1 = []
        for j in range(26):
            num = 1000
            for i in range(len(words)):
                num = min(num,words[i][j])
                if words[i][j] == 0:
                    break
            else:
                for i in range(num):
                    res1.append(chr(j + 97))
        return res1