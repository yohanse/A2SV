
    
    

from collections import deque
import heapq


n = int(input())
qualification = list(map(int, input().split()))


m = int(input())
graph = [[] for i in range(n)]
inside = [0 for i in range(n)]
for _ in range(m):
    a, b, c = list(map(int, input().split()))
    graph[a - 1].append([b - 1, c])
    inside[b - 1] += 1

count = inside.count(0)
if count > 1:
    print(-1)
else:
    heap = []
    for i in range(n):
        if inside[i] == 0:
            for a, b in graph[i]:
                heapq.heappush(heap, (b, a))
                break
    visite = set([heap])
    while heap:
        



