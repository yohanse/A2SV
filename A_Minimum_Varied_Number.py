t = int(input())
for _ in range(t):
    n = int(input())
    ans = []    
    for i in range(9, 0, -1):
        if i <= n:
            ans.append(i)
            n -= i
    ans.sort()

    r = 0
    for i in ans:
        r = r * 10 + i
    print(r)  