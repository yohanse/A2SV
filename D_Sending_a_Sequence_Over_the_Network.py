t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    dp = [False for i in range(n + 2)]
    dp[0] = True

    for i, num in enumerate(nums):
        if i - num  - 1 >= -1:
            dp[i + 1] = dp[i + 1] or dp[i - num]
        
        if i + num + 1 <= n and dp[i]:
            dp[i + num + 1] = True
        
    if dp[-1] or dp[-2]:
        print("YES")
    else:
        print("NO")

