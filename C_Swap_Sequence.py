n = int(input())
num = list(map(int, input().split()))
res = []
for i in range(n):
    index = i
    b = num[i]
    for j in range(i + 1, n):
        if b > num[j]:
            b = num[j]
            index = j
    if i != index:
        res.append([i,index])
        num[i], num[index] = num[index], num[i]
print(len(res))
for i, j in res:
    print(i, j)
