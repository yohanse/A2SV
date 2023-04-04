from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    count = Counter(nums)
    last = max(nums) + 1
    for k in range(1, 1025):
        dic = {}
        for i in nums:
            xor = i ^ k
            dic[xor] = dic.get(xor, 0) + 1
        if dic == count:
            print(k)
            break
    else:
        print(-1)
