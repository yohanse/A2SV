t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    cost = list(map(int, input().split()))
    cost_sorted = []
    for i in range(n):
        cost_sorted.append([cost[i], i])
    cost_sorted.sort()

    if n != 2 and n <= m:
        reminder = 0
        edege = []
        if m > n:
            reminder = (m - n) * (cost_sorted[0][0] + cost_sorted[1][0])
        print(sum(cost) * 2 + reminder)

        for i in range(n - 1):
            print(i + 1, i + 2)
        print(n, 1)

        for i in range(m - n):
            print(cost_sorted[0][1], cost_sorted[1][1])
    else:
        print(-1)