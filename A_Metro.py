n, e = list(map(int, input().split()))
res = []
res.append(list(input().split()))
res.append(list(input().split()))

if res[0][0] == "0":
    print("NO")
elif res[0][e - 1] == res[1][e - 1] == "0":
    print("NO")
elif res[0][e - 1] == "1":
    print("YES")
else:
    for i in range(e, n):
        if res[0][i] == res[1][i] == "1":
            print("YES")
            break
    else:
        print("NO")