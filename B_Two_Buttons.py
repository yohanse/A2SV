a, b = list(map(int, input().split()))
count = 0
while a != b:
    if b > a and b % 2 == 0:
        b //= 2
    else:
        b += 1
    count += 1
print(count)