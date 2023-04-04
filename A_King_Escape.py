from collections import deque


n = int(input())
queen_x, queen_y = list(map(int, input().split()))
king_x, king_y = list(map(int, input().split()))
final_x, final_y = list(map(int, input().split()))

grid = [[0 for i in range(n)] for j in range(n)]

direction = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, -1], [-1, 1], [-1, -1], [1, 1]]
for x, y in direction:
    i, j = queen_x - 1, queen_y - 1
    while -1 < i < n and -1 < j < n:
        grid[i][j] = 1
        i, j = i + x, j + y



def bfs(r, c, f_x, f_y, grid, directions):
    q = deque([(r, c)])

    while q:
        r, c = q.popleft()

        for x, y in directions:
            i, j  = x + r, y + c
            if -1 < i < n and -1 < j < n and grid[i][j] != 1:
                grid[i][j] = 1
                q.append((i, j))
        if r == f_x and c == f_y:
            return "YES"
    return "NO"

print(bfs(king_x - 1, king_y - 1, final_x - 1, final_y - 1, grid, direction))