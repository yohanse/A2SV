t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    best = ~0
    for i, num in enumerate(nums):
        if i != num:
            best = best & num
    print(best)