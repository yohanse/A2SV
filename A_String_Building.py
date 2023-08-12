t = int(input())

for _ in range(t):
    s = input()
    N = len(s)

    dp = [False for i in range(N + 1)]
    dp[0] = True

    can = ["aa", "aaa", "bbb", "bb"]

    for i in range(1, N):
        for w in can:
            if i - len(w) > -2:
                dp[i + 1] = dp[i + 1] or (dp[i - len(w) + 1] and w == s[i - len(w) + 1: i + 1])
    print("YES" if dp[-1] else "NO")
