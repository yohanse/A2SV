a, b = list(map(int, input().split()))
count = 0
while max(a, b) > 1 and min(a, b) > 0:
    if a > b:
        b += 1
        a -= 2
    else:
        a += 1
        b -= 2
    count += 1
print(count)