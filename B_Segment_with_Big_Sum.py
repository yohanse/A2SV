import sys
N, k = list(map(int,input().split()))
nums = list(map(int,input().split()))
slow, window_sum, res =  0, 0, sys.maxsize
for fast in range(N):
    window_sum += nums[fast]
    while window_sum >= k:
        res = min(res, fast - slow + 1)
        window_sum -= nums[slow]
        slow += 1
if res == sys.maxsize:
    print(-1)
else:
    print(res)  