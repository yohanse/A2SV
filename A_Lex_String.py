t = int(input())
for _ in range(t):
    n, m, k = list(map(int, input().split()))
    s1 = list(input())
    s2 = list(input())
    s1.sort()
    s2.sort()

    p1, p2, p3, c = 0, 0, 0, 0
    res = [0 for i in range(n + m)]
    if s1[p1] > s2[p2]:
        check = True
        p1 += 1  


    while p1 < n and p2 < m:
        if 