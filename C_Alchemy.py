n = int(input())
num = list(map(int, input().split()))
r, l = n - 1, 0
t1, t2 = 0, 0
while l <= r:
    if t1 <= t2:
        t1 += num[l]
        l += 1
    else:
        t2 += num[r]
        r -= 1
print(l,n - r -1 )

