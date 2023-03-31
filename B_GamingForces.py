t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if nums[i] == 1:
            count += 1
    ans = count // 2
    if count % 2 != 0:
        ans += count

    print(n - count + ans)
