t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    while n:
        count += 1
        n = n >> 1
    print(2 ** (count - 1) - 1)