pre = [0]*200002
n, k, q = list(map(int, input().split()))
for i in range(n):
    t1, t2 = list(map(int, input().split()))
    pre[t1] += 1
    pre[t2 + 1] -= 1

num = [0]*200002
for i in range(1,200002):
    pre[i] += pre[i-1]
    if pre[i] >= k:
        num[i] = 1   

for i in range(1,200002):
    num[i] += num[i-1]

answer = 0
for j in range(q):
    t1, t2 = list(map(int, input().split()))
    print(num[t2] - num[t1 - 1])
