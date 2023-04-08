t = int(input())
for _ in range(t):
    n = int(input())
    enemy = list(map(int, list(input())))
    george = list(map(int, list(input())))

    ans = 0
    for i in range(n):
        if enemy[i] == george[i] == 1:
            if i != 0 and enemy[i - 1] == 1:
                ans += 1
            elif i != n - 1 and enemy[i + 1] == 1:
                enemy[i + 1] = 0
                ans += 1
        elif george[i] == 1:
            ans += 1

    print(ans)