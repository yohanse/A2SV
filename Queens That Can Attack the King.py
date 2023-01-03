class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        board = [[False for i in range(8)]for j in range(8)]
        for queen_row, queen_column in queens:                  #create board and put queens by True
            board[queen_row][queen_column] = True

        king_row, king_column = king
        attacking_queen = []
        for move_row, move_column in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]:
            current_row, current_column = king_row, king_column
            while -1 < current_row < 8 and -1 < current_column < 8:
                if board[current_row][current_column]:
                    attacking_queen.append([current_row, current_column])
                    break
                current_row += move_row
                current_column +=move_column

        return attacking_queen