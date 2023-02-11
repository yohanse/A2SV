t = int(input())
for _ in range(t):
    n = int(input())
    num = list(map(int, input().split()))
    num.sort()
    l, r = 0, n - 1
    tl, tr = 0, 0
    op = "NO"
    while r >= l:
        if tr > tl and l > n - 1 - r:
            op = "YES"
            break

        elif tr <= tl:
            tr += num[r]
            r -= 1

        else:
            tl += num[l]
            l += 1
   
    if tr > tl and l > n - 1 - r:
        op = "YES"
    print(op)
