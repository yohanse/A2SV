t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    N = max(nums)

    counter = [[] for  i in range(N)]
    dp = [[0 for _ in range(N)] for i in range(n + 1)]

    for i in range(n):
        for j in range(N):
            dp[i + 1][j] = dp[i][j]
        dp[i + 1][nums[i] - 1] += 1
        counter[nums[i] - 1].append(i)
    
    ans = 1
    for num in counter:
        l, r = 0, len(num) - 1
        while r > l:
            maxi = 0
            for i in range(N):
                maxi = max(maxi, dp[num[r]][i] - dp[num[l] + 1][i])
            l, r = l + 1, r - 1
            ans = max(ans, l * 2 + maxi)
        
            
    print(ans)
