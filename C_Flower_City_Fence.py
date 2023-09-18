from collections import Counter


t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    l, r = 0, n - 1
    dic = {}
    count  = 1
    for i in range(1, n):
        if nums[i] != nums[i - 1]:
            dic[i] = nums[i - 1] - nums[i]
            count += 1
    dic[n] = nums[-1]
    dic_c = Counter(nums)
    if dic == dic_c:
        print("YES")
    else:
        print("NO")

    
        