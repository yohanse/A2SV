t = int(input())
for i in range(t):
    n = int(input())
    res = [0] * n
    l, r = 0, n - 1
    c = 0
    num = input().split()
    while l < r:
        res[c] = num[l]
        res[c + 1] = num[r]
        l += 1
        r -= 1
        c += 2
    if n % 2 == 1:
        res[c] = num[l]
    res = list(map(str,res))
    print(" ".join(res))
