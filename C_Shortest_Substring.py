t = int(input())
for i in range(t):
    n = input()
    l = 0
    num = [0, 0, 0]
    have = 0
    ans = 10**9
    for r in range(len(n)):
        if num[int(n[r]) - 1] == 0:
            have += 1

        num[int(n[r]) - 1] += 1
        while have == 3:
            num[int(n[l]) - 1] -= 1
            if num[int(n[l]) - 1] == 0:
                have -= 1
            ans = min(ans, r - l + 1)
            l += 1
    if ans == 10**9:
        ans = 0
    print(ans)