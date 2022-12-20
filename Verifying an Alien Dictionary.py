class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order={order[i]:i for i in range(26)}
        def helper(word1,word2):
            N=min(len(word1),len(word2))
            for i in range(N):
                if order[word1[i]]<order[word2[i]]:
                    return True
                if order[word1[i]]>order[word2[i]]:
                    return False
            if len(word1)<=len(word2):
                return True
            return False
        for i in range(1,len(words)):
            if helper(words[i-1],words[i])==False:
                return False
        return True