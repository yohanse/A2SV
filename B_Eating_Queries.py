t = int(input())
for _ in range(t):
    n, q = list(map(int, input().split()))

    candies = list(map(int, input().split()))
    candies.sort(reverse = True)

    for i in range(1, n):
        candies[i] += candies[i - 1]
    
    for i in range(q):
        target = int(input())
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if candies[mid] < target:
                l = mid + 1
            else:
                r = mid
        
        if candies[r] < target:
            print(-1)
        else:
            print(r + 1)