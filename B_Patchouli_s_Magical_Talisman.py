t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    to_get_odd = 64
    even_number = 0
    for num in nums:
        if num % 2 == 0:
            even_number += 1
        count = 0
        while num:
            if num & 1:
                to_get_odd = min(to_get_odd, count)
            num = num >> 1
            count += 1

    if to_get_odd == 0:
        print(even_number)
    else:
        print(to_get_odd + even_number - 1)
