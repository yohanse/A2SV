t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    divider = list(map(int, input().split()))
    divider.sort(reverse=True)
    if n <= 2:
        print(0)
    else:

        curr = 2
        for i in range(m):
            curr += divider[i] - 1
            
            if curr >= n:
                print(i + 1)
                break
        else:
            print(-1)