t = int(input())
for _ in range(t):
    n = int(input())
    string = input()
    dic = {}

    for i, s in enumerate(string):
        if s in dic:
            if dic[s] % 2 != i % 2:
                print("NO")
                break
        else:
            dic[s] = i
    else:
        print("YES")