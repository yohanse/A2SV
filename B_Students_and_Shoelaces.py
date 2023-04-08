n, m = list(map(int, input().split()))
Graph = [[] for i in range(1, n + 1)]
count = [0 for i in range(1, n + 1)]
for _ in range(m):
    s, e = list(map(int, input().split()))
    Graph[s - 1].append(e - 1)
    Graph[e - 1].append(s - 1)
    count[s - 1] += 1
    count[e - 1] += 1



res = 0
for i in range(n):
    check = False
    temp = count.copy()
    for j in range(n):
        
        if count[j] == 1:
            check = True
            for adjvertex in Graph[j]:
                temp[adjvertex] -= 1
            temp[j] -= 1
    count = temp

    if check:
        res += 1
    else:
        break

print(res)