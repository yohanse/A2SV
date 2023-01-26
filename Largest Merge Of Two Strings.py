class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        N1, N2 = len(word1), len(word2)
        l1, l2 = 0, 0
        merge = ""
        while l1 < N1 and l2 < N2:
            if word1[l1] > word2[l2]:
                merge += word1[l1]
                l1 += 1
            elif word2[l2] > word1[l1]:
                merge += word2[l2]
                l2 += 1
            else:
                if word1[l1:] > word2[l2:]:
                    merge += word1[l1]
                    l1 += 1
                elif word2[l2:] > word1[l1:]:
                    merge += word2[l2]
                    l2 += 1
                else:
                    merge += word2[l2]
                    l2 += 1
        
        
        merge += word1[l1:]
        merge += word2[l2:]
        return merge