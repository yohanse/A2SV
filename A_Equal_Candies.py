t = int(input())

for _ in range(t):
    n = int(input())
    nums= list(map(int, input().split()))

    mini = min(nums)
    ans = 0
    for i in nums:
        ans += (i - mini)
    print(ans)