def lcm(x):
    d = 2
    ans = []
    while d * d <= x:
        while x % d == 0:
            x //= d
            ans.append(d)
        d += 1
    if x != 1:
        ans.append(x)
    return ans



def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def bactrack(arr):
    n = 2 ** len(arr)
    res = []
    for i in range(1, n):
        c = 0
        ans = 1
        while i:
            if i & 1:
                ans *= arr[c]
            i = i >> 1
            c += 1
        res.append(ans)
    return res

def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l < r:
        mid = (l + r + 1) // 2
        if arr[mid] <=  target:
            l = mid
        else:
            r = mid - 1
    return arr[l]

a, b = list(map(int, input().split()))
x = gcd(a, b)
n = int(input())
arr = lcm(x)
k = bactrack(arr)
k.append(1)
k.sort()


for _ in range(n):
    low, high = list(map(int, input().split()))
    ans = binary_search(k, high)
    if high >= ans >= low:
        print(ans)
    else:
        print(-1)
    
