class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge=""
        N=min(len(word1),len(word2))
        for i in range(N):
            merge+=word1[i]+word2[i]
        return merge+word1[N:]+word2[N:]