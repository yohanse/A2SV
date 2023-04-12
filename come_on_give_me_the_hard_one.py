n = int(input())
graph = [[] for _ in range(n + 1)]
k = int(input())

for _ in range(k):
    num = list(map(int, input().split()))
    if num[0] == 1:
        graph[num[1]].append(num[2])
        graph[num[2]].append(num[1])
    else:
        print(*graph[num[1]])