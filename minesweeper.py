class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        return self.dfs(click[0], click[1], board)

    def dfs(self, r, c, board):
        n, m = len(board), len(board[0])
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, -1], [1, 1], [-1, 1], [-1, -1]]

        if board[r][c] == "M":
            board[r][c] = "X"

        else:
            count = 0
            for dx, dy in direction:
                x = r + dx
                y = c + dy

                if -1 < x < n and -1 < y < m and (board[x][y] == "X" or board[x][y] == "M"):
                    count += 1

            if not count:
                board[r][c] = "B"
                for dx, dy in direction:
                    x = r + dx
                    y = c + dy

                    if -1 < x < n and -1 < y < m and board[x][y] == "E":
                        self.dfs(x, y, board)
                        
            else:
                board[r][c] = str(count)
                
        return board