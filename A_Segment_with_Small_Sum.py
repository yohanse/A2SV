import sys

def factorial(num):
    tot = 1
    for i in range(num):
        tot += i
    return tot
N, k = list(map(int,input().split()))
nums = list(map(int,input().split()))
slow = fast = window_sum = res = 0
while fast < N:
    window_sum += nums[fast]
    count = slow
    while window_sum > k:
        window_sum -= nums[slow]
        slow += 1
    res += factorial(fast - count) - factorial(fast - slow)   
    fast += 1
print(res)       


