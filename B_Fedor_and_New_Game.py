n, m, k= list(map(int, input().split()))
army = []
for i in range(m + 1):
    army.append(int(input()))

fredo = army[-1]
friend = -1
for i in army:
    xor = fredo ^ i
    c = 0
    while xor:
        c += (xor & 1)
        xor = xor >> 1
    if c <= k:
        friend += 1
print(friend)
