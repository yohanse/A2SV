t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    for i in range(n):
        xor = nums[i]
        res = 0
        for j in range(n):
            if j != i:
                res ^= nums[j]
        if res == xor:
            print(nums[i])
            break
