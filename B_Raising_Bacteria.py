x = int(input())
c = 0
while x:
    c += x % 2
    x //= 2

print(c)