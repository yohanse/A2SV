import sys
t = int(input())
for i in range(t):
    n = int(input())
    num = list(map(int, input().split()))
    l, r = 0, n - 1
    answer = [0] * n
    def rec(l, r, t):
        if l > r:
            return
        
        mid, maxi = 0, -sys.maxsize
        for i in range(l, r + 1):
            if num[i] > maxi:
                mid, maxi = i, num[i]
        rec(mid + 1, r, t + 1)
        rec(l, mid - 1, t + 1)
        answer[mid] = t
    
    rec(l, r,  0)
    print(*answer)
