import sys
N, k = list(map(int,input().split()))
nums = list(map(int,input().split()))
slow, window_sum, res =  0, 0, 0
for fast in range(N):
    window_sum += nums[fast]
    while window_sum >= k:
        res += N - fast
        window_sum -= nums[slow]
        slow += 1
print(res)  