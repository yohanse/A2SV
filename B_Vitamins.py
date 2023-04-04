n = int(input())
juice = [-1] * 8
juice[0] = 0
for i in range(n):
    price, vitamin = list(input().split())
    c = 0
    for j in "CBA":
        if j in vitamin:
            c = c | 1
        c = c << 1
    c = c >> 1
    if juice[c] == -1:
        juice[c] = int(price)
    juice[c] = min(int(price), juice[c])

ans = -1
for i in range(8):
    for j in range(8):
        for k in range(8):
            if juice[i] != -1 and juice[j] != -1 and juice[k] != -1 and (i | j | k == 7):
                if ans == -1:
                    ans = juice[i] + juice[j] + juice[k]
                ans = min(ans, juice[i] + juice[j] + juice[k])
print(ans)