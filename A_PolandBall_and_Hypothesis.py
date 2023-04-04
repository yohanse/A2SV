n = int(input())
op = 0
for i in range(1, 1001):
    ans = n * i + 1
    d = 2
    while d * d <= ans:
        if ans % d == 0:
            op = i
            break
        d += 1
    if op:
        break
print(op)