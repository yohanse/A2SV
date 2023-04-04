n, k = list(map(int, input().split()))
xor = n ^ k
c = 0
while xor:
    c += 1
    xor = xor >> 1

print((2 ** (c) - 1))