from collections import deque


n = int(input())
graph = [set() for i in range(n)]

for i in range(n - 1):
    x, y = list(map(int, input().split()))
    graph[x - 1].add(y - 1)
    graph[y - 1].add(x - 1)

bfs = list(map(int, input().split()))
for i in range(n):
    bfs[i] -= 1

if bfs[0] != 0:
    print("No")
else:
    index = 1
    q = deque([0])
    while index < n and q:
        vertex = q.popleft()
        while index < n and bfs[index] in graph[vertex]:
            q.append(bfs[index])
            index += 1
    if index == n:
        print("Yes")
    else:
        print("No")