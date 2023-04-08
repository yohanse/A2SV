t = int(input())
for _ in range(t):
    res = []
    n = int(input())
    res.append(list(map(int, list(input()))))
    res.append(list(map(int, list(input()))))

 

    for i in range(n):
        if res[1][i] == res[0][i] == 1:
            print("NO")
            break
    else:
        print("YES")
