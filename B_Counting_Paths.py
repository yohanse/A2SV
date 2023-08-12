t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split()))

    modulo = 10 ** 9 + 7
    dp = {}
    def rec(a, b, pos):
        if a == 0:
            return b == 0
        if b < 0:
            return 0
        if (a, b, pos) in dp:
            return dp[(a, b, pos)]
        dp[(a, b, pos)] = rec(a - 1, b - 1, not pos) + rec(a - 1, b, pos)
        return dp[(a, b, pos)]
    print((2 * rec(a - 1, b, False)) % modulo)