import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

left = [1 for i in range(n)]
right = [1 for i in range(n)]

for i in range(1, n):
    if nums[i] > nums[i - 1]:
        left[i] = left[i - 1] + 1

for i in range(n - 2, -1, -1):
    if nums[i + 1] > nums[i]:
        right[i] = right[i + 1] + 1

ans = max(left)

for i in range(1, n - 1):
    if nums[i + 1] > nums[i - 1]:
        ans = max(ans, right[i + 1] + left[i - 1])
print(ans)

