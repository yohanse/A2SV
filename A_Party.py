
n = int(input())
table = {i:[] for i in range(1, n + 1)}
parent = []
for i in range(1, n + 1):
    sup = int(input())
    if sup != -1:
        table[sup].append(i)
    else:
        parent.append(i)
answer = 0
for key in parent:
    stack = [(key, 1)]
    while stack:
        root, depth = stack.pop()
        for node in table[root]:
            stack.append((node, depth + 1))
        answer = max(answer, depth)
        
print(answer)