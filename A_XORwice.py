t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    xand = n & m
    print((xand ^ n) + (xand ^ m))