n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

count = [0] * (10 ** 5 + 1)

for i in nums:
    count[i] += 1
ans = 0
nums = list(set(nums))
for i in range(len(nums)):
    for x in range(10 ** 5):
        if (x ** k) % nums[i] == 0:
            
            j = (x ** k) // nums[i]
            if j <= 10 ** 5 and count[j] != 0: 
                if nums[i] != j:
                    ans += (count[j] * count[nums[i]])

                else:
                    ans += count[j] * (count[j] - 1)
print(ans // 2)