class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        ans=[0]*(n+2)
        ans[1]=1
        leng=n//2
        for i in range(1,leng+1):
            ans[2*i]=ans[i]
            ans[2*i+1]=ans[i]+ans[i+1]
        print(ans)
        print(ans[:n+1])
        return max(ans[:n+1])