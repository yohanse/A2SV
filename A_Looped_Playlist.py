import sys
n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

t = sum(nums)
count = 1
while t < k:
    t += t
    count += 1
count += 1
    

slow = 0
tot = 0
res = [sys.maxsize, 0]
for index in range(count * n):
    index = index % n
    num = nums[index%n]
    tot += num
    while tot >= k:
        if res[0] > index - slow%n + 1:
            res[0] = index - slow%n + 1
            res[1] = slow + 1
        tot -= nums[slow]
        slow += 1
        slow = slow % n
print(res[0], res[1]%n)

