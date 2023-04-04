n = int(input())
nums = list(map(int, input().split()))

check = False
for i in range(n):
    curr = nums[i]
    for _ in range(3):
        curr = nums[curr - 1]
    if curr == nums[i]:
        print("YES")
        break
else:

    print("NO")