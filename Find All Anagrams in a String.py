class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l1 = [0]*26
        l2 = [0]*26
        res = []
        N = len(p)
        for i in p:
            l1[ord(i) - ord("a")] += 1
  
        for index, i in enumerate(s):
            l2[ord(i) - ord("a")] += 1
            for i in range(26):
                if l1[i] != l2[i]:
                    break
            else:
                res.append(index - N + 1)
                
            if index - N + 1 > -1:
                t = s[index - N + 1]
                l2[ord(t) - ord("a")] -= 1
                
        return res