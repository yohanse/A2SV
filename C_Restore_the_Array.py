t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    for i in range(1, n - 1):
        if nums[i - 1] > nums[i]:
            ans = nums[:i] + [nums[i] - 1] + nums[i:]
            print(*ans)
            break
    else:
        ans = [int(nums[0])] + nums
        print(*ans)
print(18 ^ 19)