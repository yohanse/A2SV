n, m = map(int, input().strip().split())
grid = []
direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
for i in range(n):
    x = input()
    for j in range(m):
        if x[j] == ".":
            if (i + j) % 2 == 0:
                print("B", end = "")
            else:
                print("W", end = "")
        else:
            print("-", end = "")
    print()