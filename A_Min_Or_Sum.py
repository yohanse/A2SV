t  = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    for i in range(n):
        for j in range(n):
            if i != j:
                temp = nums[i] | nums[j]
                nums[i] = 0
                nums[j] = temp
    print(sum(nums))