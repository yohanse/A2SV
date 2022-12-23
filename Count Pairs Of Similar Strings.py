class Solution:
    def similarPairs(self, words: List[str]) -> int:
        N = len(words)
        res=[]
        ans = 0
        for i in range(N):
            a=set()
            for j in words[i]:
                a.add(j)
            res.append(a)
        
        for i in range(N):
            for j in range(i+1,N):
                if res[i]==res[j]:  
                    ans+=1
        return ans   