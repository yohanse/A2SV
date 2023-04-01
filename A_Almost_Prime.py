i = int(input())
j = 0
for n in range(1, i + 1):
    temp = n
    count, d = 0, 2
    while d * d <= n:
        check = False
        while  n % d == 0:
            n //= d
            check = True
        if check:
            count += 1
        d += 1
    if n > 1:
        count += 1
    if count == 2:
        j += 1
print(j)

