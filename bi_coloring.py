def coloring(graph):
    colors = [None for _ in range(n)]
    colors[0] = True
    stack = [0]
    while stack:
        vertex = stack.pop()
        for adjvertex in graph[vertex]:
            if colors[adjvertex] == colors[vertex]:
                return "NOT BICOLOURABLE."
            
            if colors[adjvertex] == None:
                stack.append(adjvertex)
                colors[adjvertex] = not colors[vertex]
    return "BICOLOURABLE."


while True:
    n = int(input())
    if not n:
        break

    e = int(input())
    graph = [[] for _ in range(n)]
    for _ in range(e):
        a, b = list(map(int, input().split()))
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    print(coloring(graph))