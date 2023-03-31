t = int(input())
for _ in range(t):
    x = int(input())
    first_zero, first_one = 66, 66
    count = 0
    one = 0
    while x:
        if x & 1:
            one += 1
            first_zero = min(first_zero, count)
        else:
            first_one = min(first_one, count)
        count += 1
        x = x >> 1
    first_one = min(first_one, count)
    first_zero = min(first_zero, count)
    if one == 1:

        print(2 ** first_one + 2 ** first_zero)
    else:
        print(eee2 ** first_zero)
