t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    for i in range(n - 1, -1, -1):
        index = nums[i]
        if i + index < n:
            nums[i] += nums[index + i]
   
    print(max(nums))