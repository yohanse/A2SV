t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    if n > k:
        print("No")
    elif n % 2 == 0 and k % 2 == 1:
            print("No")
    else:
        num = [1] * n
        if n % 2 == 0:
             target = k - n + 2
             num[-1] = target // 2
             num[-2] = target // 2
        else:
             num[-1] = k - n + 1
        print("Yes")
        print(*num)
