t = int(input())
for _ in range(t):
    n, z = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    x = nums[0]
    for num in nums:
        x = max(num | z, x)
    print(x)