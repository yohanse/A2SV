n = int(input())
num = list(map(int, input().split()))
num.sort()
tot, tot1 = 0, 0
for i in range(n):
    tot += num[i]
for j in range(n,2*n):
    tot1 += num[j]
if tot1 == tot:
    print(-1)
else:
    num = list(map(str, num))
    print(" ".join(num))