class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row,col=len(board),len(board[0])
        def dfs(r,c):
            if r<0 or r>=row or c<0 or c>=col:
                return
            if r+1<row and board[r+1][c]=='O':
                board[r+1][c]="T"
                dfs(r+1,c)
            if r-1>-1 and board[r-1][c]=='O':
                board[r-1][c]="T"
                dfs(r-1,c)
            if c+1<col and board[r][c+1]=='O':
                board[r][c+1]="T"
                dfs(r,c+1)
            if c-1>-1 and board[r][c-1]=='O':
                board[r][c-1]="T"
                dfs(r,c-1)

        for r in range(row):
            if board[r][0]=='O':
                board[r][0]="T"
                dfs(r,0)
        
        for r in range(row):
            if board[r][col-1]=='O':
                board[r][col-1]="T"
                dfs(r,col-1)

        for c in range(col):
            if board[0][c]=='O':
                board[0][c]="T"
                dfs(0,c)
        
        for c in range(col):
            if board[row-1][c]=='O':
                board[row-1][c]="T"
                dfs(row-1,c)
        
        for r in range(row):
            for c in range(col):
                if board[r][c]=="T":
                    board[r][c]="O"
                else:
                    board[r][c]="X"

        