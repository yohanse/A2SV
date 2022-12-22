class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        table={}
        valid={2**i:0 for i in range(32)}
        res=0
        
        for i in deliciousness:
            table[i]=1+table.get(i,0)

        for i in table:
            for j in valid:
                if j-i in table:
                    if j-i==i:
                        res+=table[i]*(table[i]-1)
                    else:
                        res+=table[i]*table[j-i]
        
        res=res//2
        temp=10**9 + 7
        return res%temp