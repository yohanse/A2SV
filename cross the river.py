def coloring(vertex, graph, colors):
    colors[vertex] = True
    stack = [vertex]
    count = 0
    while stack:
        vertex = stack.pop()
        for adjvertex in graph[vertex]:
            if colors[adjvertex] == colors[vertex]:
                count += 1
            
            if colors[adjvertex] == None:
                stack.append(adjvertex)
                colors[adjvertex] = not colors[vertex]
    
    return ":)" if count < 2 else ":("


n = int(input())
graph = [[] for _ in range(n)]
colors = [None for _ in range(n)]
for i in range(n):
    num = list(map(int, input().split()))
    for j in num[1:]:
        graph[i].append(j - 1)
for i in range(n):
    if colors[i] == None and coloring(i, graph, colors) == ":(":    
        print(":(")
        break
else:
    print(":)")