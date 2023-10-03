t = int(input())

for _ in range(t):
    n = int(input())
    ans = []

    maxi = 0
    for i in range(n):
        x, y = list(map(int, input().split()))
        ans.append([x, y])
        maxi = max(maxi, x, y)

    time = [0 for i in range(maxi + 1)]
    for x, y in ans:
        time[x] += 1
        time[y] -= 1
    
    for i in range(1, maxi + 1):
        time[i] += time[i - 1]

    print(max(time))
        