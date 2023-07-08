n, d = list(map(int, input().split()))
nums = list(map(int, input().split()))

nums.sort()

l, r = 0, n - 1
c = 0
while n:
    p = nums[r]
    need = d // p + 1

    if n - need > -1:
        n -= need
        c += 1
    else:
        n = 0
    r -= 1
print(c)