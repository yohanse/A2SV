class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols,visite=len(grid),len(grid[0]),set()
        def dfs(r,c):
            res=1
            stack=[(r,c)]
            visite.add((r,c))
            while stack:
                r,c=stack.pop()
                for i,j in [[1,0],[-1,0],[0,1],[0,-1]]:
                    n_r,n_c=r+i,c+j
                    if -1<n_r<rows and -1<n_c<cols and grid[n_r][n_c]==1 and (n_r,n_c) not in visite:
                        visite.add((n_r,n_c))
                        stack.append((n_r,n_c))
                        res+=1
            return res
        ans=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visite:
                    ans=max(ans,dfs(r,c))
        return ans