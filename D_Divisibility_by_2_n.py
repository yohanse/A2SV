def how_many_time_factor_by_2(num):
    count = 0
    while num % 2 == 0:
        count += 1
        num //= 2
    return count
        




t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    total_count = 0
    max_count = []
    for i, num in enumerate(nums):
        total_count += how_many_time_factor_by_2(num)
        max_count.append(how_many_time_factor_by_2(i + 1))
    
    max_count.sort(reverse = True)
    if total_count >= n:
        print(0)
    else:
        for i in range(n):
            total_count += max_count[i]
            if total_count >= n:
                print(i + 1)
                break
        else:
            print(-1)

