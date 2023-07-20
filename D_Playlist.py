import heapq
import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))

nums = [0 for i in range(n)]
for i in range(n):
    nums[i] = list(map(int, input().split()))
    

nums.sort(key = lambda x: x[1])


total = 0
heap = []
ans = 0
for i in range(n - 1, -1, -1):

    if len(heap) == k and heap[0] < nums[i][0]:
        total -= heapq.heappop(heap)
        total += nums[i][0]
        heapq.heappush(heap, nums[i][0])
    
    if len(heap) < k:
        total += nums[i][0]
        heapq.heappush(heap, nums[i][0])
    
    ans = max(ans, total * nums[i][1])
print(ans)
        
