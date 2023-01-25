n = int(input())
res = []
for i in range(n):
    a = list(map(int, input().split()))
    res.append(a)
res.sort()

op = "Poor Alex"
mini = res[0][1]
for i in range(n):
    if res[i][1] < mini:
        op = "Happy Alex"
        break
    mini = max(mini, res[i][1])
print(op)