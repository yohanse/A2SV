import heapq


n = int(input())
m = int(input())

nums = []
for i in range(n):
    nums.append(int(input()))

ans = max(nums) + m
heapq.heapify(nums)
for i in range(m):
    heapq.heappush(nums, heapq.heappop(nums) + 1)
    
print(max(nums), ans)