n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))
queries = list(map(int, input().split()))
nums.sort()
for i in range(k):
    l, r, target = 0, n - 1, queries[i]
    while l < r:
        mid = (l + r + 1) // 2
        if nums[mid] > target:
            r = mid - 1
        else:
            l = mid

    if nums[l] == target:
        print("YES")
    else:
        print("NO")
