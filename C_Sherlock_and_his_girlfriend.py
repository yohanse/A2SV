def prime(x):
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True




n = int(input())
p = [0] * n
for i in range(n):
    if prime(i + 2):
        p[i] = 1
    else:
        p[i] = 2
            

print(max(p))
print(*p)