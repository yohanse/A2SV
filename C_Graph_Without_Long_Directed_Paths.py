from collections import deque


n, m = list(map(int, input().split()))
graph = [[] for i in range(n)]
edges = []
for i in range(m):
    a, b = list(map(int, input().split()))
    a, b = a - 1, b - 1
    edges.append(a)
    graph[a].append(b)
    graph[b].append(a)

color = [2 for i in range(m)]
    q = deque([0])
    visite =set([0])
    check = True
    while q:
        vertex = q.popleft()
        for adj in graph[vertex]:
            if color[adj] == 2:
                visite.add(adj)
                q.append(adj)
                color[adj] = 1 - color[vertex]
            if color[adj] == color[vertex]:
                return False
    return True
if check:
    ans = ""
    for a in edges:
        ans += str(color[a])

    print("YES")
    print(ans)
else:
    print("NO")

