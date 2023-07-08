import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    input()
    n, k = list(map(int, input().split()))
    stack = list(map(int, input().split()))
    for i in range(k):
        stack[i] -= 1
    
    graph = [[] for i in range(n)]
    outgoing =[0 for i in range(n)]

    for i in range(n - 1):
        a, b = list(map(int, input().split()))
        a, b = a - 1, b - 1
        graph[a].append(b)
        graph[b].append(a)
        outgoing[a] += 1
        outgoing[b] += 1
    def fun(stack):
        visite = set(stack)
        visite.add(0)
        main = set([0])

        while main:
            temp = set()
            for i in main:
                for j in graph[i]:
                    if j not in visite:
                        if outgoing[j] == 1:
                            return "YES"
                        visite.add(j)
                        temp.add(j)
            main = temp
            t = []
            for i in stack:
                for j in graph[i]:
                    if j in main:
                        main.remove(j)
                        t.append(j)
                    elif j not in visite:
                        visite.add(j)
                        t.append(j)
            stack = t
        return "NO"
    print(fun(stack))


