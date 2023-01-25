t = int(input())
for i in range(t):
    n, k = list(map(int, input().split()))
    num = list(map(int, input().split()))
    op = 0
    
    l = 0
    for i in range(1,n):
        if num[i-1] >= num[i]*2:
            if i - l > k:
                op += i - l - k
            l = i

    if n - l > k:
        op += n - l - k
    print(op)

        
