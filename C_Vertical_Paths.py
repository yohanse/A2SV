from collections import deque


t = int(input())

for _ in range(t):

    n = int(input())
    parent = list(map(int, input().split()))
    if n == 1:
        print(1)
        print(1)
        print(1)
    else:

        tree = [[] for i in range(n)]

        for i in range(n):
            parent[i] -= 1
        
        q = deque()
        setParent = set(parent)
        visite = set()
        count = 0
        for i in range(n):
            if i not in setParent:
                q.append([i, count])
                visite.add(i)
                count += 1
        ans = [[] for i in range(count)]
        
        while q:
            vertex, path = q.popleft()
            ans[path].append(vertex + 1)

            par = parent[vertex]
            if par not in  visite:
                q.append([par, path])
                visite.add(par)
        print(count)
        for i in ans:
            print(len(i))
            print(*i[::-1])
