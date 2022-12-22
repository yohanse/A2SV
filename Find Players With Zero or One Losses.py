class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        table={}
        res=[[],[]]

        for w,l in matches:
            table[w]=0
            table[l]=0
        
        for w,l in matches:
            table[l]+=1
        
        for l in table:
            if table[l]==0:
                res[0].append(l)
            elif table[l]==1:
                res[1].append(l)
                
        res[0].sort()
        res[1].sort()
        
        return res