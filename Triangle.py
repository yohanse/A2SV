class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N,dp=len(triangle),{}
        def dynamic(pos,i):
            if pos==N:return 0
            elif (pos,i) in dp:return dp[(pos,i)]
            dp[(pos,i)]=min(dynamic(pos+1,i)+triangle[pos][i],dynamic(pos+1,i+1)+triangle[pos][i+1])
            return dp[(pos,i)]
        return dynamic(1,0)+triangle[0][0]
