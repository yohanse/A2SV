t = [1, 2, 1, 2]
c = [0, 0, 0, 0]
for i in range(4):
    c[i] = t[i] ^ t[(i + 1) % 4]
print(c)