t = int(input())
for _ in range(t):
    res = []
    n = int(input())
    for i in range(n):
        res.append(input())
    a = set(res)
    for i in res:
        a.remove(i)
        check = 0
        for j in range(len(i)):
            if i[:j + 1] in a and i[j + 1:] in a:
                check = 1
                break
        a.add(i)
        print(check, end='')
    print()