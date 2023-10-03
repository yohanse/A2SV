


n, m = list(map(int, input().split()))

graph = [[] for i in range(n)]

for j in range(m):
    a, b = list(map(int, input().split()))
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
color = [2 for i in range(n)]
def Mcolor(vertex):
    color[vertex] = 0
    q = [vertex]
    while q:
        vertex = q.pop()

        for adjvertex in graph[vertex]:
            if color[adjvertex] == 2:
                color[adjvertex] = 1 - color[vertex]
                q.append(adjvertex)
                
            if color[adjvertex] == color[vertex]:
                return False
    return True

for vertex in range(n):
    if color[vertex] == 2:
        res = Mcolor(vertex)
        if not res:
            print(-1)
            break
else:
    true = [[], []]
    false = []

    for i in range(n):
        true[color[i]].append(i + 1)
    
    for i in range(2):
        print(len(true[i]))
        print(*true[i])

    

