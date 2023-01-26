t = int(input())
for _ in range(t):
    n = int(input())
    num = list(map(int, input().split()))
    num.sort()
    op = "YES"
    for i in range(1,n):
        if num[i] - num[i-1] > 1:
            op = "NO"
    print(op)