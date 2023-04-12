n = int(input())
graph = [[] for i in range(n)]
for i in range(n):
    num = list(map(int, input().split()))
    for j in range(n):
        if num[j]:
            graph[i].append(j + 1)
for i in range(n):
    print(len(graph[i]), *graph[i])