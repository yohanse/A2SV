q = int(input())

for _ in range(q):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        arr[i] -= 1
    ans = [-1 for i in range(n)]
    visite = set()
    for i in range(n):
        curr = arr[i]
        count = 0
        while curr not in visite:
            visite.add(curr)
            curr = arr[curr]
            count += 1

        curr = arr[i]
        for i in range(count):
            ans[curr] = count
            curr = arr[curr]
    print(*ans)
