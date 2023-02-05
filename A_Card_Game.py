n = int(input())
num = list(map(int,input().split()))

l, r = 0, n - 1
t, t1 = 0, 0
check = True
while l <= r:
    if num[l] > num[r]:
        if check:
            t += num[l]
        else:
            t1 += num[l]
        l += 1
    else:
        if check:
            t += num[r]
        else:
            t1 += num[r]
        r -= 1
    check = not check
    
print(t, t1)
        
