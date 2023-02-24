t = int(input())
for _ in range(t):
    n, m, k = list(map(int, input().split()))
    a = list(input())
    b = list(input())
    a.sort()
    b.sort()
    p1, p2 = 0, 0
    ans = ""
    c = 0
    while p1 < n and p2 < m:

        
        while p1 < n and a[p1] < b[p2] and c < k:
            ans += a[p1]
            p1 += 1
            c += 1
        
        if p1 == n:
            break
        p = 0
        if c == k:
            ans += b[p2]
            p2 += 1
            p = 1

        while p2 < m and a[p1] > b[p2] and p < k:
            ans += b[p2]
            p2 += 1
            p += 1
        
        if p2 == m:
            break
        
        c = 0
        if p == k:
            ans += a[p1]
            p1 += 1
            c = 1
            

    print(ans)
            


