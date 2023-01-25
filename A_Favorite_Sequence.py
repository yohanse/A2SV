t = int(input())
for _ in range(t):
    n = int(input())
    res = [0]*n
    num = list(map(int, input().split()))
    l, r, i = 0, n-1, 0
    check = False
    while r >= l:
        if check:
            res[i] = num[r]
            r -= 1
        else:
            res[i] = num[l]
            l += 1

        i += 1
        check = not check
        
    res = list(map(str, res))
    print(' '.join(res))

