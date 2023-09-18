t = int(input())

for _ in range(t):
    n = int(input())
    a, b = set(), set()
    res = []
    for i in range(n):
        c, d = list(map(int, input().split()))
        res.append([min(c, d), max(c, d)])
    res.sort()

    for c, d in res:
        if c == d:
            print("NO")
            break
        if c not in a and d not in a:
            a.add(c)
            a.add(d)
        elif c not in b and d not in b:
            b.add(c)
            b.add(d)
        else:
            print("NO")
            break
    else:
        print("YES")