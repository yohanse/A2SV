class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        count_X = 0
        count_O = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'O':
                    count_O += 1
                elif board[i][j] == 'X':
                    count_X += 1
        if count_X < count_O or count_X > count_O + 1:
            return False
        elif self.winner(board) == 'X' and count_X == count_O:
            return False
        elif self.winner(board) == 'O' and count_X != count_O:
            return False
        return True
    def winner(self,board):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2]:
                return board[i][0]
            elif board[0][i] == board[1][i] == board[2][i]:
                return board[0][i]
        if board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]
        elif board[2][0] == board[1][1] == board[0][2]:
            return board[2][0]