n = int(input())
x = list(map(int, input().split()))
color = list(map(int, input().split()))

graph = {i: [] for i in range(n)}
for i in range(n - 1):
    s = x[i] - 1
    graph[s].append(i + 1)

res = 1
stack = [0]
while stack:
    curr = stack.pop()
    for adjvertex in graph[curr]:
        y = 1 if color[curr] != color[adjvertex] else 0
        res += y
        stack.append(adjvertex)
        
print(res) 