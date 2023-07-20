s = input()

dp = [[False, False] for i in range(len(s))]
dpb = [[False, False] for i in range(len(s))]

for i in range(1, len(s)):
    dp[i][0] = dp[i - 1][0] or s[i - 1: i + 1] == 'AB'
    dp[i][1] = dp[i - 1][1] or s[i - 1: i + 1] == 'BA'

for i in range(len(s) - 2, -1, -1):
    dpb[i][0] = dpb[i + 1][0] or s[i: i + 2] == 'AB'
    dpb[i][1] = dpb[i + 1][1] or s[i: i + 2] == 'BA'

flag = False
for i in range(1, len(s)):
    if (dp[i - 1][0] and dpb[i][1]) or (dp[i - 1][1] and dpb[i][0]):
        flag = True
        break

print("YES" if flag else "NO")
