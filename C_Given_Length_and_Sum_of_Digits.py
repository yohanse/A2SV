import sys
n, m = list(map(int, input().split()))
dp = {}
def rec(index, total):
    if total < 0:
        return -sys.maxsize, sys.maxsize
    
    if index == n:
        if total:
            return -sys.maxsize, sys.maxsize
        return 0, 0
    
    if (index, total) in dp:
        return dp[(index, total)]
    
    mini = sys.maxsize
    maxi = -sys.maxsize
    for i in range(10):
        if index == 0 and i == 0:
            continue

        ans1, ans2 = rec(index + 1, total - i)
        mini = min(ans2 * 10 + i, mini)
        maxi = max(maxi, ans1 * 10 + i)
    dp[(index, total)] = (maxi, mini)
    return maxi, mini
 
if m == 0 or m > n * 9:
    print(-1, -1)
else:
    ans1, ans2 = rec(0, m)
    print(ans2, ans1)
 