n = int(input())
res = 0
for i in range(n):
    num = list(map(int, input().split()))
    for j in range(n):
        if num[j]:
            res += 1
print(res // 2)