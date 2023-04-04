n, m  = list(map(int, input().split()))

grid = []
for i in range(n):
    grid.append(list(input()))

direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
check = True
for r in range(n):
    for c in range(m):
        if grid[r][c] != ".":
            for x, y in direction:
                i, j = r + x, c + y
                if -1 < i < n and -1 < j < m and ((grid[r][c] == "S" and grid[i][j] == "W") or (grid[r][c] == "W" and grid[i][j] == "S")):
                    check = False

        else:
            grid[r][c] = "D"
        


if check:
    print("Yes")
    for i in range(n):
        print("".join(grid[i]))
else:
    print("NO")