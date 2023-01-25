n = int(input())
num = list(map(int, input().split()))
l, r = 0, n - 1
tot1, tot2 = 0, 0
check = True
while r >= l:
    if num[l] > num[r]:
        if check:
            tot1 += num[l]
        else:
            tot2 += num[l]
        l += 1
    else:
        if check:
            tot1 += num[r]
        else:
            tot2 += num[r]
        r -= 1
    check = not check
print(tot1, tot2)

