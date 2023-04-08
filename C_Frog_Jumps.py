t = int(input())
for _ in range(t):
    moves = input()

    l = 0
    ans = 0
    N = len(moves)
    while l < N:
        r = l
        while r < N and moves[r] == "L":
            r += 1
        ans = max(ans, r - l)
        l = r + 1
    print(ans + 1)