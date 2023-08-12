from bisect import bisect_right


t = int(input())
for _ in range(t):
    n, s  = list(map(int, input().split()))
    num = list(map(int, input().split()))
    origin = num.copy()
    for i in range(1, n):
        num[i] += num[i - 1]

    if num[-1] <= s:
        print(0)
    else:
        ans = [0, bisect_right(num, s)]
        for i in range(n):
            if i > 0 and num[i - 1] >= s:
                break
            
            if ans[1] < bisect_right(num, s + origin[i]):
                ans = [i + 1, bisect_right(num, s + origin[i])]
        print(ans[0])

