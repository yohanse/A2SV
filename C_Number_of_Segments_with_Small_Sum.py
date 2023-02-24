def factorial(num):
    return (num*(num - 1))/2

N, k = list(map(int,input().split()))
nums = list(map(int,input().split()))
slow = fast = window_sum = res = 0
while fast < N:
    window_sum += nums[fast]
    count = slow
    while window_sum > k:
        window_sum -= nums[slow]
        slow += 1
    res += factorial(fast - count + 1) - factorial(fast - slow + 1)
    fast += 1
res += factorial(fast - slow + 1) 
print(int(res)) 