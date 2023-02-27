from collections import deque


N,k = list(map(int,input().split()))
d = list(map(int,input().split()))
p = list(map(int,input().split()))
index = [ i for i in range(N)]
index.sort(key = lambda x : p[x])
right = 0
for _ in range(k):
    ans = 0
    ty,am = list(map(int,input().split()))
    ans += min(d[ty - 1],am) * p[ty - 1]
    d[ty - 1] -= am 
    if d[ty - 1] < 0:
        am = -(d[ty - 1 ])
    else:
        am = 0
    d[ty - 1] = max(d[ty -1],0)

    while am > 0 and right < len(p) :
        ans += min(d[index[right]],am) * p[index[right]]
        d[index[right]] -= am 
        if d[index[right]] < 0:
            am = -d[index[right]]
            d[index[right]] = 0
            right += 1
        else:
            am = 0
        
    if am > 0:
        ans = 0
    
    print(ans)