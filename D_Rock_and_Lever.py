t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    counter = {}
    for i, num in enumerate(nums):
        c = 0
        while num:
            c += 1
            num >>= 1 
        nums[i] = c

    for i in nums:
        counter[i] = counter.get(i, 0) + 1
        
    ans = 0
    for i in counter:
        n = counter[i]
        ans += ((n - 1)*n) // 2
    print(ans)
