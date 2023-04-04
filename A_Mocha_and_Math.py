t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    xand = nums[0]
    for i in nums:
        xand = xand & i
    print(xand)