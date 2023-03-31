t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    red = 0
    blue = nums[0]
    l, r = 1, n - 1
    ans = "NO"
    while l < r:
        red += nums[r]
        blue += nums[l]
        if red > blue:
            ans = "YES"
        r -= 1
        l += 1
    print(ans)
        