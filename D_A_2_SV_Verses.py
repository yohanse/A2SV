from bisect import bisect_left, bisect_right


n, a, b = list(map(int, input().split()))

nums = list(map(int, input().split()))
num_copy = nums.copy()
for i in range(1, n):
    nums[i] += nums[i - 1]

answer = 0
nums = [0] + nums

for i in range(n):

    left = bisect_left(nums, nums[i] + a)
    right = bisect_right(nums, nums[i] + b)
    
    answer += right - left
    
print(answer)
