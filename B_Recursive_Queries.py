ans = [0]
def recur(l, r, k):
    if int(k) > r:
        return 0
    if int(k) > l:
        ans[0] += 1
    
    for i in k:
        for j in range(1, k):
            if 




q = int(input())
for _ in range(q):
    l, r, k = list(map(int, input().split()))
