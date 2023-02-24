n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))
data = {}
have = 0
slow = 0
res = 0
for index, num in enumerate(nums):
    if data.get(num, 0) == 0:
        data[num] = 1
        have += 1
    else:
        data[num] += 1
    while have > k:
        res += index - slow
        data[nums[slow]] -= 1
        if data[nums[slow]] == 0:
            have -= 1
        slow += 1
for i in range(slow, n):
    res += index - i + 1
print(res)
    

