n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))
res = 1
maximum, minimum = [[nums[0], 0]], [[nums[0], 0]]
slow = 0
for index in range(1, n):
    num = nums[index]
    
    while maximum and maximum[-1][0] < num:
        maximum.pop()
    maximum.append([num, index])

    while minimum and minimum[-1][0] > num:
        minimum.pop()
    minimum.append([num, index])
    
    while maximum[0][0] - minimum[0][0] > k:
        if maximum[0][1] == slow:
            maximum.pop(0)
        if minimum[0][1] == slow:
            minimum.pop(0)
        slow += 1

    res += index - slow + 1
print(res)