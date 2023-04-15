n = int(input())

edge = n * (n - 1) // 2 - 1
graph = [[0, 0, i + 1] for i in range(n)]

for _ in range(edge):
    a, b =list(map(int, input().split()))
    graph[a - 1][0] += 1
    graph[a - 1][1] += 1
    graph[b - 1][1] += 1


graph.sort(reverse = True)
for i in range(n):
    if graph[i][1] != n - 1:
        print(graph[i][2], end = " ")