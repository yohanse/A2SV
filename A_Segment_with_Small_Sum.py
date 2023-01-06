N, k = list(map(int,input().split()))
nums = list(map(int,input().split()))
slow = fast = window_sum = res = 0
while fast < N:
    window_sum += nums[fast]
    if window_sum > k:
        window_sum -= nums[slow]
        slow += 1
    res = max(res, fast - slow + 1)
    fast += 1
print(res)       


