n, t = list(map(int, input().split()))
nums = list(map(int, input().split()))
curr = 1
while curr < t:
    curr += nums[curr - 1]
if curr == t:
    print("YES")
else:
    print("NO")