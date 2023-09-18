from collections import deque


n, m = list(map(int, input().split()))
res = [0 for i in range(n)]
q = deque()
for i in range(n):
    res[i] = list(map(int, input().split()))
    q.append((i, res[i][0], res[i][1]))


graph = [[]for i in range(n + m)]
for j in range(m):
    maxi, con = list(map(int, input().split()))
    graph[con].append((maxi, j + n))
print(graph)
print(0)
ans= [0, 0]
while q:
    v, m, b = q.popleft()
    for maxi, adj in graph[v]:
        if len(graph[v]) != m:
            print(v)
            if ans[0] < b // (len(graph[v]) + 1):
                
                
                ans = [b // (len(graph[v]) + 1), v]
        q.append((adj, maxi, b // len(graph[i])))
print(ans)