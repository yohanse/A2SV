n, m = list(map(int, input().split()))
dic = {}
color = {}
for i in range(n):
    x = input()
    dic[x] = []
    color[x] = 2

for i in range(m):
    a, b = input().split()
    dic[a].append(b)
    dic[b].append(a)


can = []
visite = set()
for i in dic:
    if len(dic[i]) == 0:
        can.append(i)
    else:
        if color[i] == 2:
            color[i] = 0
            q = [i]
            while q:
                v = q.pop()
                for a in dic[v]:
                    if dic

