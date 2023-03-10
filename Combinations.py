class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans1=[]
        def back(n,k,pos=0,j=0,ans=[]):
            if k==j:
                ans1.append(ans)
                return 
            for i in range(1,n+1):
                if i>pos:
                    back(n,k,i,j+1,ans+[i])
        back(n,k)
        return ans1