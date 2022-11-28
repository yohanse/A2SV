class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row,col,dp=len(grid),len(grid[0]),{}
        def dynamic(r,c):
            if (r==row and c==col-1) or (r==row-1 and c==col):
                return 0
            elif (r,c) in dp:
                return dp[(r,c)]
            elif r==row:
                return 10000000000
            elif c==col:
                return 100000000000
            dp[(r,c)]=min(dynamic(r+1,c)+grid[r][c],dynamic(r,c+1)+grid[r][c])
            return dp[(r,c)]
        return dynamic(0,0)