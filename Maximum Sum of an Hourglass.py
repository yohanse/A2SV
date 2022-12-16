class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        
        for i in range(row):
            tot=0
            for j in range(col):
                grid[i][j]=tot+grid[i][j]
                tot=grid[i][j]

        ans=0
        for i in range(row-2):
            for j in range(col-2):
                if j>=1:ans=max(ans,grid[i][j+2]-grid[i][j-1]+grid[i+2][j+2]-grid[i+2][j-1]+grid[i+1][j+1]-grid[i+1][j])
                else:ans=max(ans,grid[i][j+2]+grid[i+2][j+2]+grid[i+1][j+1]-grid[i+1][j])
                
        return ans