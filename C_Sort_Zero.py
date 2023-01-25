t = int(input())
for _ in range(t):
    n = int(input())
    num = list(map(int,input().split()))
    op = 0
    for i in range(1,n):
        if num[i-1] > num[i]:
            op += 1
    print(op)
