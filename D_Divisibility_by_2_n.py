t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    count, k = 0, 0
    ans = []
    for i in range(n):
        temp = i + 1
        ic = 0
        while temp % 2 == 0:
            temp //= 2
            ic += 1
        ans.append(ic)

        while nums[i] % 2 == 0:
            count += 1
            nums[i] //= 2

    need = n - count
    operation = 0
    ans.sort()
    k = n - 1
    while need > 0 and k > -1:
        need -= ans[k]
        k -= 1
        operation += 1

    if need < 1:
        print(operation)

    else:
        print(-1)