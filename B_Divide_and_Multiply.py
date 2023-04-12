t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort()

    c = 1
    for i in range(len(nums)):
        while nums[i] % 2 == 0:
            nums[i] //= 2
            c *= 2
    maxi = max(nums)
    print(maxi * c + (sum(nums) - maxi))

    