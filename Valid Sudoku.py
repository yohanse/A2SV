class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        matr = defaultdict(set)
        for r in range(9):
            for c in range(9):
                i, j = r//3, c//3
                if board[r][c] != '.':
                    if board[r][c] in cols[c] or board[r][c] in rows[r] or board[r][c] in matr[(i,j)]:
                        return False
                    cols[c].add(board[r][c])
                    rows[r].add(board[r][c])
                    matr[(i,j)].add(board[r][c])
        return True