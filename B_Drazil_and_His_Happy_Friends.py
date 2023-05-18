n, m = list(map(int, input().split()))

happy_boy = list(map(int, input().split()))
happy_girl = list(map(int, input().split()))

boy = [False] * n
girl = [False] * m

for i in happy_boy[1:]:
    boy[i] = True

for i in happy_girl[1:]:
    girl[i] = True

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

lcm = n * m // gcd(n, m)

graph_boy = [[] for i in range(n)]
graph_girl = [[] for i in range(m)]

for i in range(lcm + 1):
    graph_boy[i % n].append(i % m)
    graph_girl[i % m].append(i % n)

visite = set()

for i in range(n):
    if (i, True) not in visite:
        ans = False
        q = [(i, True)]
        visite.add((i, True))
        while q:
            vertex, boz = q.pop()
            
            if boz:
                ans = ans or boy[vertex]
                for adjvertex in graph_boy[vertex]:
                    if (adjvertex, False) not in visite:
                        visite.add((adjvertex, False))
                        q.append((adjvertex, False))
            else:
                ans = ans or girl[vertex]
                for adjvertex in graph_girl[vertex]:
                    if (adjvertex, True) not in visite:
                        visite.add((adjvertex, True))
                        q.append((adjvertex, True))

        if ans == False:
            print("No")
            break
else:
    print("Yes")
