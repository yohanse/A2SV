t = int(input())

for _ in range(t):
    n = int(input())
    res = []
    for i in range(n):
        a, b = tuple(map(int, input().split()))
        res.append((b - a, a, b))
    res.sort(reverse = True)

    for i in range(n):
        if res[i][1] == res[i][2]:
            print(res[i][1], res[i][1], res[i][1])
        else:
            for j in range(i + 1, n):
                if res[i][1] == res[j][1]:
                    print(res[i][1], res[i][2], res[j][2] + 1)
                    break

                if res[i][2] == res[j][2]:
                    print(res[i][1], res[i][2], res[j][1] - 1)
                    break
        
    print()
