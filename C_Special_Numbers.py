t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))

    c = 0
    ans = 0
    while k:
        if k & 1:
            ans += n ** c
        k = k >> 1
        c += 1
    print(ans % (10 **9 + 7))