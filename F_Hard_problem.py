
n = int(input())
cost = list(map(int, input().split()))
words = []
index = {}
for i in range(n):
    x = input().strip()
    words.append(x)

dp = {(0, True):cost[0], (0, False):0}

for i in range(1, n):
    count = 0
    if words[i] >= words[i - 1]:
        if (i - 1, False) in dp:
            dp[(i, False)] = dp[(i - 1, False)]
            count += 1
    
    if words[i][::-1] >= words[i - 1]:
        if (i - 1, False) in dp:
            dp[(i, True)] = dp[(i - 1, False)] + cost[i]
            count += 1
    
    if words[i] >= words[i - 1][::-1]:
        if (i - 1, True) in dp:
            dp[(i, False)] = min(dp.get((i, False), float("inf")), dp[(i - 1, True)])
            count += 1
    
    if words[i][::-1] >= words[i - 1][::-1]:
        if (i - 1, True) in dp:
            dp[(i, True)] = min(dp.get((i, True), float("inf")), dp[(i - 1, True)] + cost[i])
            count += 1

    if count == 0:
        print(-1)
        break

else:
    print(min(dp.get((n - 1, True), float("inf")), dp.get((n - 1, False), float("inf"))))