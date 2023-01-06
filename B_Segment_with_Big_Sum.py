N, k = list(map(int,input().split()))
nums = list(map(int,input().split()))
slow, fast, window_sum, res = 0, 0, 0, 100000
while fast < N:
    window_sum += nums[fast]
    while window_sum >= k:
        res = min(res, fast - slow + 1)
        window_sum -= nums[slow]
        slow += 1
    
    fast += 1
print(res)  