class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row,col=len(board),len(board[0])
        def dfs(r,c):
            for i,j in [[0,1],[0,-1],[1,0],[-1,0]]:
                Nr,Nc=r+i,c+j
                if -1<Nr<row and -1<Nc<col and board[Nr][Nc]=='O':
                    board[Nr][Nc]="T"
                    dfs(Nr,Nc)

        for i,j in [[0,row],[col-1,row]]:
            for k in range(j):
                if board[k][i]=="O":
                    board[k][i]="T"
                    dfs(k,i)
        
        for i,j in [[0,col],[row-1,col]]:
            for k in range(j):
                if board[i][k]=="O":
                    board[i][k]="T"
                    dfs(i,k)


        
        for r in range(row):
            for c in range(col):
                if board[r][c]=="T":
                    board[r][c]="O"
                else:
                    board[r][c]="X"