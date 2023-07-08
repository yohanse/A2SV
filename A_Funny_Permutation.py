t = int(input())
for _ in range(t):
    n = int(input())
    if n == 3:
        print(-1)
        
    elif n == 5:
        print(5, 4, 1, 2, 3)
    else:
        result = [i for i in range(n, 0, -1)]
        if n % 2:
            result[n // 2], result[n // 2 - 1] = result[n // 2 - 1], result[n // 2]
        print(*result)