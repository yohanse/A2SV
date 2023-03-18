t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))
    index = list(map(int, input().split()))
    num = []
    last = index[-1]
    index.sort()
    for i in range(m):
        if i == 0:
            num.append(n - index[-1] + index[i] - 1)
        else:
            num.append(index[i] - index[i - 1] - 1)
    num.sort(reverse = True)
    minu = 0
    ans = 0
    for i in num:
        if i - minu <= 0:
            break
        if i - minu == 1:
            ans += 1
     
        else:
        
            ans += i - minu - 1
        minu += 4

    print(n - ans)