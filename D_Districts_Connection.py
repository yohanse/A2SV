from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    gang = list(map(int, input().split()))
    graph = defaultdict(list)
    for i in range(n):
        band = gang[i]
        graph[band].append(i)
    
    if len(graph) == 1:
        print("NO")
    else:
        print("YES")
        best = gang[0]
        second = 0
        for i in gang:
            if i != best:
                second = i
                break

        v1, v2 = graph[best][0], graph[second][0]

        for i in graph:
            if i != best:
                for j in graph[i]:
                    print(v1 + 1, j + 1)

        for j in graph[best][1:]:
            print(v2 + 1, j + 1)
        


    