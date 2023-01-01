N = int(input())
bar = list(map(int, input().split()))
l, r = 0, N - 1
alice, bob = 0, 0
while l <= r:
    if alice > bob:
        bob += bar[r]
        r -= 1
    else:
        alice += bar[l]
        l += 1
print(l ,N - l)